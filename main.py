#!/usr/bin/env python3
"""Entrypoint: copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR deterministically."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(HERE, "entry.png")
TARGET = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

def main():
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    shutil.copyfile(ASSET, TARGET)
    print("wrote", TARGET, os.path.getsize(TARGET), "bytes")

if __name__ == "__main__":
    main()
