"""Carousels v8 (15/11/2026): python3 make_car.py spec.json -> out/<id>/c_NN.jpg (1080x1350)"""
import json, sys, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
S = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = HERE / "out" / S["id"]; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{HERE}/car.html"); pg.wait_for_selector('body[data-ready="1"]')
    n = len(S["slides"])
    for i, s in enumerate(S["slides"], 1):
        pg.evaluate("([s,i,n]) => show(s,i,n)", [s, i, n]); pg.wait_for_timeout(150)
        pg.locator("#s").screenshot(path=str(out / f"c_{i:02d}.jpg"), type="jpeg", quality=93)
    b.close()
print(out)
