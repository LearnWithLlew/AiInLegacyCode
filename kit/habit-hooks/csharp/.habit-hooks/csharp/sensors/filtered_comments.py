"""Run the csharp plugin's comment tool, dropping license headers and XML doc comments."""

import json
import subprocess
import sys
from pathlib import Path

import habit_hooks_csharp

TOOL = Path(habit_hooks_csharp.__file__).parent / "comment-tool/bin/Release/net8.0/comment-tool.dll"


def header_length(path: str) -> int:
    """Number of leading lines that are comments or blank (the license header)."""
    count = 0
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip() and not line.lstrip().startswith("//"):
            break
        count += 1
    return count


def is_reportable(issue: dict, headers: dict) -> bool:
    details = issue["details"]
    if details["message"].startswith("doc-line comment"):
        return False
    return details["line"] > headers[details["file"]]


def main() -> int:
    files = sys.argv[sys.argv.index("--") + 1 :]
    result = subprocess.run(["dotnet", str(TOOL), *files], capture_output=True, encoding="utf-8")
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        return result.returncode
    findings = json.loads(result.stdout or "[]")
    headers = {f: header_length(f) for f in files if Path(f).is_file()}
    for finding in findings:
        finding["issues"] = [i for i in finding["issues"] if is_reportable(i, headers)]
    print(json.dumps([f for f in findings if f["issues"]]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
