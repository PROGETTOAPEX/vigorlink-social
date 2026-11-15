"""Device-in-scene slides (Andrea 15/11/2026: 'telefono e computer in scena'). python3 make_mock.py spec.json"""
import json, sys, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
S = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = HERE / "out" / S["id"]; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.goto(f"file://{HERE}/mock.html"); pg.wait_for_selector('body[data-ready="1"]')
    n = S.get("n", len(S["slides"]))
    for i, s in enumerate(S["slides"], 1):
        pg.evaluate("([s,i,n]) => show(s,i,n)", [s, s.get("i", i), n]); pg.wait_for_timeout(200)
        pg.locator("#s").screenshot(path=str(out / f"c_{i:02d}.jpg"), type="jpeg", quality=94)
    b.close()
print(out)
