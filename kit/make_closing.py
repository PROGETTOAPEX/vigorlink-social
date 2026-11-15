"""Reel with the animated closing (decision of Andrea 15/11/2026, claude/CHIUSURA_REEL_ANIMATA_15NOV2026.md).
python3 make_closing.py spec.json [fondatori|attesa] [black|light|orange]  -> out/<id>/silent_chiusura.mp4
Colour scheme follows the reel (decision of Andrea 15/11/2026: closing in our three colours).
The reel body runs until the black end layer has covered the recap (w3 + 1.0 s), then chiusura/chiusura.mp4
(2.6 s) and a hold of its last frame. 'attesa' redraws the bottom line as "Lista d'attesa · link in bio"."""
import json, subprocess, sys, pathlib, tempfile
from PIL import Image, ImageDraw, ImageFont
HERE = pathlib.Path(__file__).parent
spec = json.loads(pathlib.Path(sys.argv[1]).read_text()); variant = sys.argv[2] if len(sys.argv) > 2 else 'fondatori'
scheme = sys.argv[3] if len(sys.argv) > 3 else (spec.get('bg') or 'orange')
out = HERE / 'out' / spec['id']; out.mkdir(parents=True, exist_ok=True)
tmp = pathlib.Path(tempfile.mkdtemp())
body = dict(spec, id=spec['id'] + '__body', dur=round(spec['w3'] + 1.0, 2), closing={'black':'#000','light':'#F3EFE8','orange':'#FF6A13'}[scheme])
(tmp / 'body.json').write_text(json.dumps(body))
subprocess.run(['python3', str(HERE / 'make.py'), str(tmp / 'body.json')], check=True)
body_mp4 = HERE / 'out' / body['id'] / 'silent.mp4'
close = HERE / 'chiusura' / 'chiusura.mp4'
import numpy as np
BG = {'light': (243, 239, 232), 'orange': (255, 106, 19)}
def recolor(im):
    """The closing is light on black: alpha = brightness. Above the text (logo, sparks, glow): light scheme keeps
    the orange and turns white-hot cores orange; orange scheme turns all the light white. Text area: white
    words turn black, the orange 2027 stays orange on light and turns white on orange."""
    a = np.asarray(im, dtype=np.float32) / 255
    mx = a.max(axis=2, keepdims=True); mn = a.min(axis=2, keepdims=True)
    alpha = np.clip((mx - 0.05) / 0.95, 0, 1)          # drop the near-black vignette
    sat = np.where(mx > 0.02, (mx - mn) / np.maximum(mx, 1e-3), 0)
    col = a / np.maximum(mx, 1e-3)
    text = np.zeros_like(alpha); text[1000:] = 1          # rows of the words
    orange = np.array([1.0, 0.42, 0.075], dtype=np.float32)
    sf = np.clip(sat * 2.2, 0, 1)
    if scheme == 'light':
        logo = col * sf + orange * (1 - sf)                 # hot white cores -> orange
        words = col * sf                                    # white -> black, 2027 orange stays
    else:
        logo = np.ones_like(a)                              # all the light -> white
        words = np.ones_like(a) * sf                        # white -> black, 2027 -> white
    fg = logo * (1 - text) + words * text
    bg = np.array(BG[scheme], dtype=np.float32) / 255
    out = bg * (1 - alpha) + fg * alpha
    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))
sys.path.insert(0, str(HERE / 'chiusura'))
from clean_logo import build
MASK, GRAD = build(HERE / 'chiusura' / 'last.png')
from PIL import ImageFilter
RING = np.asarray(Image.fromarray((MASK[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(91)).filter(ImageFilter.GaussianBlur(30))).astype(np.float32)[..., None] / 255
GLOW = np.asarray(Image.fromarray((MASK[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(28))).astype(np.float32)[..., None] / 255
def clean_logo(im, k):
    """From the fill onwards the symbol is redrawn with a clean outline (Andrea 15/11/2026)."""
    a = np.asarray(im, dtype=np.float32) / 255
    if scheme == 'black':
        bg = np.zeros(3, np.float32); base = bg + GRAD * GLOW * 0.55; logo = GRAD
    else:
        bg = np.array(BG[scheme], dtype=np.float32) / 255; base = np.broadcast_to(bg, a.shape)
        logo = GRAD if scheme == 'light' else np.ones_like(a)
    clean = base * (1 - MASK) + logo * MASK
    w = RING * k
    return Image.fromarray((np.clip(a * (1 - w) + clean * w, 0, 1) * 255).astype(np.uint8))
if True:
    fr = tmp / 'fr'; fr.mkdir()
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(close), str(fr / 'f%03d.png')], check=True)
    font = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', 40)
    BOX = (200, 1540, 880, 1640)
    for f in sorted(fr.glob('*.png')):
        im = Image.open(f).convert('RGB')
        # brightness of the original line = its fade-in; reuse it for the new words
        reg = im.crop(BOX).convert('L'); a = max(reg.getextrema()[1] - 20, 0) / 210
        if variant == 'attesa':
            d = ImageDraw.Draw(im); d.rectangle(BOX, fill=(0, 0, 0))
            txt = "Lista d'attesa · link in bio"; w = d.textlength(txt, font=font)
            c = int(min(a, 1) * 225)
            d.text(((1080 - w) / 2, 1565), txt, font=font, fill=(c, c, c))
        if scheme != 'black': im = recolor(im)
        n = int(f.stem[1:]) - 1                               # frame index (f001 = 0)
        k = min(max((n - 30) / 8, 0), 1)
        if k > 0: im = clean_logo(im, k)
        im.save(f)
    close = tmp / 'close.mp4'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-framerate', '30', '-i', str(fr / 'f%03d.png'), '-c:v', 'libx264', '-crf', '16', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', str(close)], check=True)
res = out / 'silent_chiusura.tmp.mp4'
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(body_mp4), '-i', str(close),
  '-filter_complex', '[0:v]fps=30,format=yuv420p,setsar=1[a];[1:v]fps=30,format=yuv420p,setsar=1,tpad=stop_mode=clone:stop_duration=2.2[b];[a][b]concat=n=2:v=1[v]',
  '-map', '[v]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(res)], check=True)
res.rename(out / 'silent_chiusura.mp4'); print(out / 'silent_chiusura.mp4')
