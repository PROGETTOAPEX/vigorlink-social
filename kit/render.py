"""Render VigorLink social posts (stills 4:5 + 9:16, and optional reels) from posts.json."""
import json
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
OUT = HERE / "out"
FPS = 30


def wait_imgs(pg):
    """Screenshots (logo, phone, laptop) must be loaded before a slide is photographed."""
    pg.wait_for_function("Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)", timeout=15000)


def stills(b, post, outdir):
    n = len(post["slides"])
    for w, h, tag in [(1080, 1350, "ig"), (1080, 1920, "tt")]:
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(f"file://{HERE}/engine.html?w={w}&h={h}")
        pg.wait_for_selector('body[data-ready="1"]')
        for i, sc in enumerate(post["slides"], 1):
            total = 1 if post.get("single") else n
            pg.evaluate("([sc, o]) => show(sc, o)", [sc, {"mode": "still", "idx": i, "total": total}])
            wait_imgs(pg)
            pg.wait_for_timeout(150)
            name = f"{tag}_{i:02d}.png" if n > 1 else f"{tag}.png"
            pg.locator("#stage").screenshot(path=str(outdir / name))
        pg.close()


def reel(b, post, outdir):
    frames = outdir / "_frames"
    frames.mkdir(exist_ok=True)
    for f in frames.glob("*.jpg"):
        f.unlink()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(f"file://{HERE}/engine.html?w=1080&h=1920")
    pg.wait_for_selector('body[data-ready="1"]')
    for sc in post["reel"]:  # load every image once, so the first frames are never empty
        pg.evaluate("([sc, o]) => show(sc, o)", [sc, {"mode": "reel", "t": 1.0, "gt": 1.0}])
        wait_imgs(pg)
    k, gt = 0, 0.0
    for sc in post["reel"]:
        dur = sc["dur"]
        for j in range(int(dur * FPS)):
            t = j / FPS
            pg.evaluate("([sc, o]) => show(sc, o)", [sc, {"mode": "reel", "t": t, "gt": gt + t}])
            pg.locator("#stage").screenshot(path=str(frames / f"{k:05d}.jpg"), type="jpeg", quality=90)
            k += 1
        gt += dur
    pg.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(frames / "%05d.jpg"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-movflags", "+faststart",
                    str(outdir / "reel.mp4")], check=True)
    for f in frames.glob("*.jpg"):
        f.unlink()
    frames.rmdir()


def default_dur(sc):
    t = sc["type"]
    if t == "list":
        return 2.6 + 1.5 * len(sc["items"])
    if t == "compare":
        return 2.4 + 1.2 * len(sc["rows"])
    return {"hero": 3.4, "device": 3.8, "stat": 3.6, "cta": 4.0, "strike": 2.8}.get(t, 3.5)


def main():
    args = sys.argv[1:]
    src = next((a for a in args if a.endswith(".json")), "posts.json")
    posts = json.loads((HERE / src).read_text())
    only = set(a for a in args if not a.endswith(".json"))
    what = {a.split(":")[1] for a in only if a.startswith("only:")}
    only = {a for a in only if not a.startswith("only:")}
    with sync_playwright() as p:
        b = p.chromium.launch()
        for post in posts:
            if only and post["id"] not in only:
                continue
            outdir = OUT / post["id"]
            outdir.mkdir(parents=True, exist_ok=True)
            if not what or "stills" in what:
                stills(b, post, outdir)
            if post.get("reel") == "auto":
                post["reel"] = [dict(sc, dur=sc.get("dur") or default_dur(sc)) for sc in post["slides"]]
            if post.get("reel") and (not what or "reel" in what):
                reel(b, post, outdir)
            print("done", post["id"], flush=True)
        b.close()


if __name__ == "__main__":
    main()
