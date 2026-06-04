#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const http = require("http");
const https = require("https");

const PROVIDERS = [
  { provider: "openai", mode: "api", env: ["OPENAI_API_KEY"], base: 88, reasons: ["api_key_detected", "high_storyvista_fit", "supports_character_portraits", "supports_location_keyart"], region: "global" },
  { provider: "google", mode: "api", env: ["GOOGLE_API_KEY", "GEMINI_API_KEY"], base: 84, reasons: ["api_key_detected", "global_provider", "supports_multimodal_generation"], region: "global" },
  { provider: "stability", mode: "api", env: ["STABILITY_API_KEY"], base: 78, reasons: ["api_key_detected", "stable_diffusion_ecosystem"], region: "global" },
  { provider: "flux", mode: "api", env: ["BFL_API_KEY"], base: 82, reasons: ["api_key_detected", "high_location_keyart_quality"], region: "global" },
  { provider: "replicate", mode: "api", env: ["REPLICATE_API_TOKEN"], base: 76, reasons: ["api_key_detected", "multi_model_api"], region: "global" },
  { provider: "leonardo", mode: "api", env: ["LEONARDO_API_KEY"], base: 72, reasons: ["api_key_detected", "concept_art_workflow"], region: "global" },
  { provider: "ideogram", mode: "api", env: ["IDEOGRAM_API_KEY"], base: 70, reasons: ["api_key_detected", "good_text_rendering"], region: "global" },
  { provider: "fal", mode: "api", env: ["FAL_KEY"], base: 74, reasons: ["api_key_detected", "developer_model_hosting"], region: "global" },
  { provider: "together", mode: "api", env: ["TOGETHER_API_KEY"], base: 68, reasons: ["api_key_detected", "developer_model_hosting"], region: "global" },
  { provider: "qwen-image", mode: "api", env: ["DASHSCOPE_API_KEY", "QWEN_API_KEY", "ALIBABA_CLOUD_API_KEY_ID", "ALIBABA_CLOUD_API_KEY_SECRET"], base: 90, reasons: ["api_key_detected", "mainland_china_friendly", "chinese_prompt_support"], region: "china" },
  { provider: "minimax-image", mode: "api", env: ["MINIMAX_API_KEY"], base: 80, reasons: ["api_key_detected", "mainland_china_friendly"], region: "china" },
  { provider: "tencent-hunyuan-image", mode: "api", env: ["TENCENTCLOUD_SECRET_ID", "TENCENTCLOUD_SECRET_KEY"], base: 82, reasons: ["api_key_detected", "mainland_china_friendly", "cloud_provider"], region: "china" },
  { provider: "baidu-wenxin-image", mode: "api", env: ["BAIDU_API_KEY", "BAIDU_SECRET_KEY"], base: 74, reasons: ["api_key_detected", "mainland_china_friendly"], region: "china" },
  { provider: "zhipu-image", mode: "api", env: ["ZHIPUAI_API_KEY"], base: 66, reasons: ["api_key_detected", "china_provider_candidate"], region: "china" },
  { provider: "volcengine-seedream", mode: "api", env: ["VOLCENGINE_ACCESS_KEY", "VOLCENGINE_SECRET_KEY"], base: 78, reasons: ["api_key_detected", "seedream_candidate"], region: "china" },
  { provider: "comfyui", mode: "api", env: ["COMFYUI_API_URL"], base: 76, reasons: ["local_endpoint_configured", "supports_custom_workflow"], region: "local", endpoint: true },
  { provider: "automatic1111", mode: "api", env: ["AUTOMATIC1111_API_URL", "SD_WEBUI_API_URL"], base: 72, reasons: ["local_endpoint_configured", "stable_diffusion_local"], region: "local", endpoint: true },
  { provider: "local-image-provider", mode: "api", env: ["LOCAL_IMAGE_PROVIDER_URL"], base: 64, reasons: ["local_endpoint_configured"], region: "local", endpoint: true }
];

const MANUAL_ENV = ["STORYVISTA_IMAGE_ASSETS_DIR", "STORYVISTA_MANUAL_ASSETS_DIR", "STORYVISTA_IMAGE_MANIFEST_PATH"];
const PROMPT_ONLY_PROVIDERS = new Set(["midjourney", "jimeng", "jianying"]);
const PLACEHOLDER_PROVIDERS = new Set(["placeholder-svg"]);

function parseArgs(argv) {
  const opts = { json: false, verify: false, noNetwork: false, config: "image-provider.config.yaml" };
  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--json") opts.json = true;
    else if (arg === "--verify") opts.verify = true;
    else if (arg === "--no-network") opts.noNetwork = true;
    else if (arg === "--config" && argv[i + 1]) opts.config = argv[++i];
  }
  return opts;
}

function maskSecret(value) {
  if (!value) return "";
  if (value.length <= 8) return `${value.slice(0, 2)}***`;
  return `${value.slice(0, 3)}***${value.slice(-4)}`;
}

function readConfig(configPath) {
  if (!fs.existsSync(configPath)) return null;
  const text = fs.readFileSync(configPath, "utf8");
  const pick = (key) => {
    const match = text.match(new RegExp(`^\\s*${key}:\\s*["']?([^"'\\n#]+)`, "m"));
    return match ? match[1].trim() : null;
  };
  return { path: configPath, mode: pick("mode"), provider: pick("provider"), raw_present: true };
}

function endpointReachable(url) {
  return new Promise((resolve) => {
    try {
      const client = url.startsWith("https") ? https : http;
      const req = client.get(url, { timeout: 2000 }, (res) => {
        res.resume();
        resolve(res.statusCode < 500);
      });
      req.on("timeout", () => {
        req.destroy();
        resolve(false);
      });
      req.on("error", () => resolve(false));
    } catch {
      resolve(false);
    }
  });
}

function scoreProvider(def, detectedSignals, verified, status) {
  let score = def.base;
  const risk = [];
  const reasons = [...def.reasons];
  if (verified) {
    score += 8;
    reasons.unshift("verified_api_available");
  } else if (status === "unreachable") {
    risk.push("provider_unreachable");
  } else {
    risk.push("provider_configured_but_unverified");
  }
  if (detectedSignals.length > 1) {
    score += 2;
    reasons.push("multiple_config_signals_detected");
  }
  return { score: Math.max(0, Math.min(100, score)), selection_reason: reasons, risk_reasons: risk };
}

function modeForConfiguredProvider(provider, configuredMode) {
  if (configuredMode) return configuredMode;
  if (PROMPT_ONLY_PROVIDERS.has(provider)) return "prompt-only";
  if (PLACEHOLDER_PROVIDERS.has(provider)) return "placeholder-svg";
  if (provider === "manual-assets" || provider === "local-folder") return "manual-assets";
  return "api";
}

function statusForMode(mode) {
  if (mode === "prompt-only") return "prompt_only";
  if (mode === "placeholder-svg") return "placeholder_only";
  if (mode === "manual-assets") return "requires_manual_setup";
  return "configured_but_unverified";
}

function riskForMode(mode) {
  if (mode === "prompt-only") return ["prompt_only"];
  if (mode === "placeholder-svg") return ["placeholder_only"];
  if (mode === "manual-assets") return ["selected_provider_requires_manual_generation"];
  return ["provider_configured_but_unverified"];
}

async function main() {
  const opts = parseArgs(process.argv);
  const config = readConfig(opts.config);
  const detected = [];

  for (const def of PROVIDERS) {
    const signals = def.env.filter((name) => process.env[name]);
    if (!signals.length) continue;
    let verified = false;
    let status = "detected";
    if (def.endpoint && opts.verify && !opts.noNetwork) {
      const url = process.env[signals[0]];
      verified = await endpointReachable(url);
      status = verified ? "reachable" : "unreachable";
    }
    const scored = scoreProvider(def, signals, verified, status);
    detected.push({
      provider: def.provider,
      source: def.endpoint ? "local_endpoint" : "environment_variable",
      signals,
      masked_signals: Object.fromEntries(signals.map((name) => [name, maskSecret(process.env[name])])),
      status,
      verified,
      safe_to_use: verified ? "yes" : "unknown",
      mode: def.mode,
      score: scored.score,
      selection_reason: scored.selection_reason,
      risk_reasons: scored.risk_reasons,
      notes: verified ? "Availability was verified." : "Detected configuration, but no test call was made."
    });
  }

  for (const name of MANUAL_ENV) {
    const value = process.env[name];
    if (!value) continue;
    const exists = fs.existsSync(path.resolve(value));
    detected.push({
      provider: name === "STORYVISTA_IMAGE_MANIFEST_PATH" ? "manual-assets" : "local-folder",
      source: name === "STORYVISTA_IMAGE_MANIFEST_PATH" ? "existing_manifest" : "manual_assets_dir",
      signals: [name],
      masked_signals: { [name]: value },
      status: exists ? "detected" : "configured_but_unverified",
      verified: exists,
      safe_to_use: exists ? "yes" : "unknown",
      mode: "manual-assets",
      score: exists ? 70 : 56,
      selection_reason: exists ? ["manual_assets_available"] : ["manual_assets_configured"],
      risk_reasons: exists ? [] : ["provider_configured_but_unverified"],
      notes: exists ? "Manual asset path exists." : "Manual asset path was configured but not found."
    });
  }

  if (config && config.provider && config.provider !== "auto") {
    const existing = detected.find((item) => item.provider === config.provider);
    if (existing) {
      existing.score = Math.min(100, existing.score + 6);
      existing.selection_reason.unshift("explicit_user_config");
    } else {
      const configuredMode = modeForConfiguredProvider(config.provider, config.mode);
      detected.push({
        provider: config.provider,
        source: "config_file",
        signals: [config.path],
        masked_signals: {},
        status: statusForMode(configuredMode),
        verified: false,
        safe_to_use: "unknown",
        mode: configuredMode,
        score: configuredMode === "placeholder-svg" ? 40 : configuredMode === "prompt-only" ? 52 : 58,
        selection_reason: ["explicit_user_config", `${configuredMode}_configured`],
        risk_reasons: riskForMode(configuredMode),
        notes: "Provider was configured in image-provider config but no availability signal was detected."
      });
    }
  }

  detected.sort((a, b) => b.score - a.score);
  const selected = detected[0] || null;
  const fallback = {
    provider: "placeholder-svg",
    selected_mode: "placeholder-svg",
    score: 40,
    selection_reason: ["no_directly_callable_provider_detected", "auto_fallback"],
    risk_reasons: ["no_provider_detected", "placeholder_only"]
  };
  const autoSelection = selected ? {
    enabled: true,
    selected_provider: selected.provider,
    selected_mode: selected.mode,
    score: selected.score,
    selection_reason: ["highest_scoring_detected_provider", ...selected.selection_reason],
    risk_reasons: selected.risk_reasons,
    manual_override_available: true
  } : {
    enabled: true,
    selected_provider: fallback.provider,
    selected_mode: fallback.selected_mode,
    score: fallback.score,
    selection_reason: fallback.selection_reason,
    risk_reasons: fallback.risk_reasons,
    manual_override_available: true
  };

  const status = selected
    ? (selected.status === "configured_but_unverified" ? "provider_configured_but_unverified" : "provider_detected")
    : "no_provider_detected";
  const report = {
    storyvista_image_provider_report: {
      status,
      config_file: config ? { path: config.path, mode: config.mode, provider: config.provider } : null,
      detected_providers: detected,
      auto_selection: autoSelection,
      missing_recommended_providers: PROVIDERS.flatMap((def) => def.env).filter((name) => !process.env[name]).slice(0, 12),
      selected_mode: autoSelection.selected_mode,
      recommended_next_steps: selected ? [
        "Continue with the recommended image provider.",
        "Or configure another image provider in image-provider.config.yaml.",
        "Or continue with prompt-only mode and generate images externally."
      ] : [
        "Continue with prompt-only or semantic placeholder mode.",
        "Configure an image provider later and regenerate visual assets.",
        "Provide manual images and bind them through image-manifest.json."
      ],
      user_facing_message: selected
        ? `StoryVista selected ${autoSelection.selected_provider} for image asset generation or planning.`
        : "Current environment has no directly callable image provider. StoryVista will continue with prompts, image-manifest.json, and semantic placeholders."
    }
  };

  const output = JSON.stringify(report, null, 2);
  console.log(output);
  process.exit(selected ? 0 : 1);
}

main().catch((error) => {
  const report = {
    storyvista_image_provider_report: {
      status: "detection_failed_non_blocking",
      detected_providers: [],
      auto_selection: {
        enabled: true,
        selected_provider: "placeholder-svg",
        selected_mode: "placeholder-svg",
        score: 40,
        selection_reason: ["detection_failed_non_blocking", "auto_fallback"],
        manual_override_available: true
      },
      selected_mode: "placeholder-svg",
      recommended_next_steps: ["Continue with semantic placeholders.", "Run diagnosis again later."],
      user_facing_message: "Image provider diagnosis failed non-blocking; StoryVista can continue with semantic placeholders.",
      error: String(error && error.message ? error.message : error)
    }
  };
  console.log(JSON.stringify(report, null, 2));
  process.exit(2);
});
