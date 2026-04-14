#!/usr/bin/env python3
"""Render verification screenshots for L-1261."""
from playwright.sync_api import sync_playwright

HTML_PATH = "file:///Users/Shared/projects/hp-demo/L-1261/index-v6.html"
OUT_DIR = "/Users/Shared/projects/hp-demo/L-1261"

with sync_playwright() as p:
    b = p.chromium.launch()
    # Desktop
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.goto(HTML_PATH)
    page.wait_for_timeout(2500)
    page.screenshot(path=f"{OUT_DIR}/v6-desktop.png", full_page=True)
    print("Desktop screenshot saved.")
    ctx.close()
    # Mobile
    ctx2 = b.new_context(viewport={"width": 375, "height": 812}, device_scale_factor=2)
    page2 = ctx2.new_page()
    page2.goto(HTML_PATH)
    page2.wait_for_timeout(2500)
    page2.screenshot(path=f"{OUT_DIR}/v6-mobile.png", full_page=True)
    print("Mobile screenshot saved.")
    ctx2.close()
    b.close()
print("Done.")
