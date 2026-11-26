"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single line, 1 to 240 characters: a quiet, earned
moment of pride for someone in a scene.
After three years of night shifts, she finally held the
certificate in hands that had never stopped shaking — and smiled
like the whole ward was hers. Small person, hard road, long
effort finally landing. That is the pride.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
