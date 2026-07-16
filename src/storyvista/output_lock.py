from __future__ import annotations

import hashlib
import json
import os
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, TextIO

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows fallback
    fcntl = None
    import msvcrt


class OutputBusyError(OSError):
    pass


def _lock_path(output_dir: Path) -> Path:
    digest = hashlib.sha256(str(output_dir).encode("utf-8")).hexdigest()
    lock_dir = Path(tempfile.gettempdir()) / "storyvista-output-locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    return lock_dir / f"{digest}.lock"


def _try_lock(handle: TextIO) -> bool:
    if fcntl is not None:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return False
        return True

    handle.seek(0)
    if not handle.read(1):
        handle.seek(0)
        handle.write("\0")
        handle.flush()
    handle.seek(0)
    try:
        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        return False
    return True


def _unlock(handle: TextIO) -> None:
    if fcntl is not None:
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return
    handle.seek(0)
    msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)


def _holder_summary(handle: TextIO) -> str:
    try:
        handle.seek(0)
        holder = json.loads(handle.read() or "{}")
    except (OSError, json.JSONDecodeError):
        return ""
    details = [str(holder.get("operation", "")).strip(), f"pid {holder.get('pid')}" if holder.get("pid") else ""]
    return ", ".join(item for item in details if item)


@contextmanager
def output_lock(output_dir: str | Path, operation: str) -> Iterator[None]:
    output = Path(output_dir).resolve()
    lock_path = _lock_path(output)
    handle = lock_path.open("a+", encoding="utf-8")
    if not _try_lock(handle):
        holder = _holder_summary(handle)
        handle.close()
        suffix = f" ({holder})" if holder else ""
        raise OutputBusyError(f"StoryVista output is already being modified: {output}{suffix}")

    try:
        handle.seek(0)
        handle.truncate()
        json.dump(
            {
                "output_dir": str(output),
                "operation": operation,
                "pid": os.getpid(),
                "started_at": datetime.now(timezone.utc).isoformat(),
            },
            handle,
            ensure_ascii=False,
        )
        handle.flush()
        yield
    finally:
        _unlock(handle)
        handle.close()
