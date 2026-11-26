#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261125 bounty.

'Wednesday Full Edition' — a dense newspaper front page built from
30 dated stories first reported on Wednesday 25 November 2026,
spread across 9 regions, with a UTC timeline strip and a date-check
audit panel.

The front page itself is pre-rendered into entry.png (drawn by
draw.py, sitting in this same folder). All this program does is
carry that finished image into the output directory make.fun
provides. Standard library only, no network access, no randomness:
running it twice produces byte-identical output every time.

It never deletes anything — it only copies one file in.
"""

import os
import shutil


def pick_target():
    """Return the full path the front page should be copied to.

    MAKEFUN_OUTPUT_DIR may point at a directory (the usual case) or
    directly at a .png file; both are honoured.
    """
    given = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if given.endswith(".png"):
        return given
    return os.path.join(given, "entry.png")


def main():
    destination = pick_target()

    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)

    here = os.path.dirname(os.path.abspath(__file__))
    rendered = os.path.join(here, "entry.png")

    shutil.copyfile(rendered, destination)
    print("wrote", destination)


if __name__ == "__main__":
    main()
