#!/usr/bin/env python3
"""make.fun entry: news-image-20261125 ("Wednesday Full Edition").

Copies the pre-rendered front page (entry.png, built by draw.py) to the
make.fun output directory. Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if out_dir.endswith(".png"):
        dest = out_dir
    else:
        dest = os.path.join(out_dir, "entry.png")
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
