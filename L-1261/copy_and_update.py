#!/usr/bin/env python3
"""Copy index-v6.html to index.html."""
import shutil
shutil.copy2(
    "/Users/Shared/projects/hp-demo/L-1261/index-v6.html",
    "/Users/Shared/projects/hp-demo/L-1261/index.html"
)
print("Copied index-v6.html -> index.html")
