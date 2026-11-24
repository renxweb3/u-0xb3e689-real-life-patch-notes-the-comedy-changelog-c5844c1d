#!/usr/bin/env python3
"""Real-Life Patch Notes — one changelog line, entry.txt."""
import os
from pathlib import Path


def changelog_line():
    version = "v2.4.1"
    fix = ("fixed a bug where the human body requested a software update "
           "(sleep) every night and ignored the 'remind me later' button.")
    return f"{version}: {fix}"


def main():
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(changelog_line(), encoding="utf-8")
    print("wrote", target)


if __name__ == "__main__":
    main()
