"""Run the bundled kordoc CLI without npm or network access (Python 3.12+)."""

from __future__ import annotations

import os
from pathlib import Path
import platform
import stat
import subprocess
import sys


def main() -> int:
    skill_dir = Path(__file__).resolve().parent.parent
    machine = platform.machine().lower()
    if machine not in {"x86_64", "amd64"}:
        print(f"지원하지 않는 CPU: {machine} (x64 필요)", file=sys.stderr)
        return 2

    if sys.platform == "win32":
        node = skill_dir / "runtime" / "win32-x64" / "node.exe"
    elif sys.platform.startswith("linux"):
        node = skill_dir / "runtime" / "linux-x64" / "node"
    else:
        print(f"지원하지 않는 운영체제: {sys.platform}", file=sys.stderr)
        return 2

    cli = skill_dir / "node_modules" / "kordoc" / "dist" / "cli.js"
    if not node.is_file() or not cli.is_file():
        print("kordoc 번들 파일이 없습니다. ZIP 전체를 다시 풀어 주세요.", file=sys.stderr)
        return 2

    if sys.platform.startswith("linux") and not os.access(node, os.X_OK):
        try:
            node.chmod(node.stat().st_mode | stat.S_IXUSR)
        except OSError as exc:
            print(f"Node 실행 권한을 설정할 수 없습니다: {exc}", file=sys.stderr)
            return 2

    env = os.environ.copy()
    env["KORDOC_OFFLINE"] = "1"
    try:
        return subprocess.run([str(node), str(cli), *sys.argv[1:]], env=env, check=False).returncode
    except OSError as exc:
        print(f"kordoc 실행 실패: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
