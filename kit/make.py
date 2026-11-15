"""v8 Reels (15/11/2026): one continuous timeline, 30 fps. python3 make.py spec.json [t ...] (stills at t)"""
import json, subprocess, sys, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
S = json.loads(pathlib.Path(sys.argv[1]).read_text()); ts = [float(x) for x in sys.argv[2:]]
out = HERE / "out" / S["id"]; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(f"file://{HERE}/reel.html"); pg.wait_for_selector('body[data-ready="1"]')
    if ts:
        for t in ts:
            pg.evaluate("([s,t]) => show(s,t)", [S, t]); pg.locator("#stage").screenshot(path=str(out / f"s_{t:05.2f}.jpg"), type="jpeg", quality=88)
    else:
        tmp = out / "silent.tmp.mp4"
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", "30", "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(tmp)], stdin=subprocess.PIPE)
        for k in range(round(S["dur"] * 30)):
            pg.evaluate("([s,t]) => show(s,t)", [S, k / 30])
            ff.stdin.write(pg.locator("#stage").screenshot(type="jpeg", quality=92))
        ff.stdin.close(); assert ff.wait() == 0
        tmp.rename(out / "silent.mp4")
    b.close()
