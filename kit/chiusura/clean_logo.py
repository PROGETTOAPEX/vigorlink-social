"""Clean logo for the settled part of the animated closing (Andrea 15/11/2026: "pulisci i contorni del logo").
The outline comes from the app icon (public/icons/icon-512.png, crisp edges), scaled onto the symbol of the
closing; the colour is the closing's own yellow->orange gradient, sampled per row from the core."""
import numpy as np
from PIL import Image, ImageFilter
HERE = __import__('pathlib').Path(__file__).parent
def build(last_png, W=1080, H=1920):
    ic = Image.open(HERE / 'icon-512.png').convert('RGB'); hsv = np.asarray(ic.convert('HSV')).astype(np.float32)
    soft = np.clip((hsv[..., 2] - 140) / 60, 0, 1) * (hsv[..., 1] > 110)
    x0, x1, y0, y1 = 114, 403, 142, 377                       # symbol box in the icon
    crop = Image.fromarray((soft[y0:y1, x0:x1] * 255).astype(np.uint8))
    bx, by, bw, bh = 265, 425, 547, 443                       # symbol box in the closing
    big = crop.resize((bw * 4, bh * 4), Image.LANCZOS).filter(ImageFilter.GaussianBlur(11))
    big = big.point(lambda v: 255 if v > 128 else 0).filter(ImageFilter.GaussianBlur(1.5))
    m = big.resize((bw, bh), Image.LANCZOS)
    mask = np.zeros((H, W), np.float32); mask[by:by + bh, bx:bx + bw] = np.asarray(m).astype(np.float32) / 255
    a = np.asarray(Image.open(last_png).convert('RGB')).astype(np.float32)
    lh = np.asarray(Image.open(last_png).convert('RGB').convert('HSV')).astype(np.float32)
    core = (mask > 0.9) & (lh[..., 2] > 170) & (lh[..., 1] > 120)
    cnt = core.sum(axis=1); ys = np.where(cnt > 10)[0]
    rows = np.array([np.median(a[y][core[y]], axis=0) for y in ys])
    k = np.ones(21) / 21
    sm = np.stack([np.convolve(np.pad(rows[:, c], 10, mode='edge'), k, mode='valid') for c in range(3)], 1)
    full = np.stack([np.interp(np.arange(H), ys, sm[:, c]) for c in range(3)], 1)
    color = np.repeat(full[:, None, :], W, axis=1) / 255
    return mask[..., None], color
