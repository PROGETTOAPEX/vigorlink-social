"""Animated carousel slide: the laptop screen plays a live recording (15/11/2026).
python3 make_mock_video.py intro/P2.json <slide index, 0-based> <frames dir> <out.mp4>"""
import json, sys, pathlib, subprocess
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).parent.resolve()
S = json.loads(pathlib.Path(sys.argv[1]).read_text()); k = int(sys.argv[2]); fr = sorted((H / sys.argv[3]).glob('f*.jpg')); outp = pathlib.Path(sys.argv[4]); TARGET = sys.argv[5] if len(sys.argv) > 5 else 'laptop'
n = len(S['slides']) + sum(1 for x in S['slides'] if x.get('ex')) + 2
i = 2 + sum(2 if x.get('ex') else 1 for x in S['slides'][:k])
s = S['slides'][k]
d = {"bg": "black", "t": s['t'], "b": s['b']}
if s.get('ph'):
    d['laptop'] = {"img": "", "x": 40, "y": 470, "w": 900, "ry": 10, "rx": 2}
    d['phone'] = {"img": s['ph'], "x": 690, "y": 560, "w": 340, "ry": -12, "rx": 2}
else:
    d['laptop'] = {"img": "", "x": 66, "y": 520, "w": 948, "ry": 6, "rx": 2}
tmp = outp.with_suffix('.tmp.mp4')
ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", "25", "-c:v", "mjpeg", "-i", "-", "-vf", "fps=30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(tmp)], stdin=subprocess.PIPE)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{H}/mock.html"); pg.wait_for_selector('body[data-ready="1"]')
    d[TARGET]['img'] = str(fr[0].relative_to(H))
    if TARGET == 'phone': d['laptop']['img'] = s['pc']
    pg.evaluate("([s,i,n]) => show(s,i,n)", [d, i, n]); pg.wait_for_timeout(300)
    img = pg.locator('.lid img')
    for f in fr:
        pg.evaluate("([src,SEL]) => { const im = document.querySelector(SEL); im.src = src; return im.decode() }", [str(f.relative_to(H)), '.lid img' if TARGET == 'laptop' else '.phone img'])
        ff.stdin.write(pg.locator('#s').screenshot(type='jpeg', quality=93))
    b.close()
ff.stdin.close(); assert ff.wait() == 0; tmp.rename(outp); print(outp, i, n)
