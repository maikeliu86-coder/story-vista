# Visual Provider Preflight

Provider preflight records configuration signals in `provider-choice-state.json`. It never prints keys, auto-installs a model, creates an account, or makes a paid call.

Selection rules:

1. Explicit user configuration wins.
2. One detected configuration signal may be recommended, but remains unverified until a runtime check succeeds.
3. Multiple signals require a user-facing recommendation rather than silent provider switching.
4. No verified provider creates a prompt-ready workflow; `placeholder-svg` remains the final display fallback.
5. Manual assets and prompt-only export remain valid modes.

Mainland-accessible and global provider recommendations are maintained separately because availability, pricing, and policy change. Users perform installation and account setup themselves.
