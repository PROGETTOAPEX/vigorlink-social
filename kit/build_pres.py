"""Presentation carousels (15/11/2026): orange cover (car.html) + device slides (mock.html) + black end (car.html).
python3 build_pres.py spec.json -> out/<id>/c_01..c_NN.jpg"""
import json, sys, pathlib
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).parent.resolve(); S = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = H / 'out' / S['id']; out.mkdir(parents=True, exist_ok=True)
for f in out.glob('c_*.jpg'): f.unlink()
n = len(S['slides']) + sum(1 for x in S['slides'] if x.get('ex')) + 2
END = {"type": "end", "t": ["In arrivo", "nel primo", "trimestre <span style='color:#FF6A13'>2027</span>"], "s": S.get('endS', "Per personal trainer, fisioterapisti e nutrizionisti. Entra in lista: ti avvisiamo al lancio."), "p": "Lista d'attesa: link in bio"}
def dev(s, i):
    bg = 'black' if i % 2 == 0 else 'light'
    d = {"bg": bg, "t": s['t'], "b": s['b']}
    if s.get('ph2'):
        d['phone'] = {"img": s['ph'], "x": 130, "y": 470, "w": 390, "ry": 12, "rx": 2}
        d['phone2'] = {"img": s['ph2'], "x": 560, "y": 520, "w": 390, "ry": -12, "rx": 2}
    elif s.get('ph'):
        d['laptop'] = {"img": s['pc'], "x": 40, "y": 470, "w": 900, "ry": 10, "rx": 2}
        d['phone'] = {"img": s['ph'], "x": 690, "y": 560, "w": 340, "ry": -12, "rx": 2}
    else:
        d['laptop'] = {"img": s['pc'], "x": 66, "y": 520, "w": 948, "ry": 6, "rx": 2}
    return d
plan = []   # (engine, slide, index)
i = 1
for s in S['slides']:
    i += 1; plan.append(('mock', dict(dev(s, 0)), i))
    if s.get('ex'):
        i += 1; plan.append(('car', {"type": "list", "bg": "light", "check": 1, "t": s['ext'], "items": s['ex']}, i))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{H}/car.html"); pg.wait_for_selector('body[data-ready="1"]')
    for s, k in [(dict(S['cover'], type='cover', bg='orange'), 1), (END, n)] + [(s, k) for e, s, k in plan if e == 'car']:
        pg.evaluate("([s,i,n]) => show(s,i,n)", [s, k, n]); pg.wait_for_timeout(150)
        pg.locator('#s').screenshot(path=str(out / f'c_{k:02d}.jpg'), type='jpeg', quality=94)
    pg.goto(f"file://{H}/mock.html"); pg.wait_for_selector('body[data-ready="1"]')
    for e, s, k in plan:
        if e != 'mock': continue
        pg.evaluate("([s,i,n]) => show(s,i,n)", [s, k, n]); pg.wait_for_timeout(200)
        pg.locator('#s').screenshot(path=str(out / f'c_{k:02d}.jpg'), type='jpeg', quality=94)
    b.close()
print(out)
