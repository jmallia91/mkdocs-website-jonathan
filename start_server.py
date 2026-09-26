"""Start the local MkDocs preview with Windows/Anaconda support."""

import os
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent
    env = os.environ.copy()
    conda_bin = Path(sys.base_prefix) / "Library" / "bin"
    if sys.platform == "win32" and (conda_bin / "cairo.dll").exists():
        env["PATH"] = str(conda_bin) + os.pathsep + env.get("PATH", "")
        dll_paths = env.get("CAIROCFFI_DLL_DIRECTORIES", "")
        env["CAIROCFFI_DLL_DIRECTORIES"] = str(conda_bin) + (
            os.pathsep + dll_paths if dll_paths else ""
        )
    certificates = root / ".venv" / "windows-ca.pem"
    if certificates.exists():
        env.setdefault("REQUESTS_CA_BUNDLE", str(certificates))
    try:
        return subprocess.call(
            [sys.executable, "-m", "mkdocs", "serve", *sys.argv[1:]],
            cwd=root,
            env=env,
        )
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
