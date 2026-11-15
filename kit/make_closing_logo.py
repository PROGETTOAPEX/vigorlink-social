"""Logo-only animated closing for the video slides of the carousels (decision of Andrea 15/11/2026:
"solo con il logo, senza in arrivo etc."). Builds chiusura/logo_1350.mp4 (1080x1350, black) and appends it.
python3 make_closing_logo.py in.mp4 out.mp4"""
import subprocess, sys, pathlib, tempfile
import numpy as np
from PIL import Image, ImageFilter
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE / 'chiusura'))
from clean_logo import build
LOGO = HERE / 'chiusura' / 'logo_1350.mp4'
Y0, HOLD, XF = 15, 1.0, 0.35
if not LOGO.exists():
    MASK, GRAD = build(HERE / 'chiusura' / 'last.png')
    m = Image.fromarray((MASK[..., 0] * 255).astype(np.uint8))
    RING = np.asarray(m.filter(ImageFilter.MaxFilter(91)).filter(ImageFilter.GaussianBlur(30))).astype(np.float32)[..., None] / 255
    GLOW = np.asarray(m.filter(ImageFilter.GaussianBlur(28))).astype(np.float32)[..., None] / 255
    clean = (GRAD * GLOW * 0.55) * (1 - MASK) + GRAD * MASK
    keep = np.clip((1000 - np.arange(1920)) / 50, 0, 1).astype(np.float32)[:, None, None]   # words start ~y1037
    tmp = pathlib.Path(tempfile.mkdtemp()); fr = tmp / 'fr'; fr.mkdir()
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(HERE / 'chiusura' / 'chiusura.mp4'), str(fr / 'f%03d.png')], check=True)
    for f in sorted(fr.glob('*.png')):
        a = np.asarray(Image.open(f).convert('RGB'), dtype=np.float32) / 255 * keep
        k = min(max((int(f.stem[1:]) - 1 - 30) / 8, 0), 1); w = RING * k
        a = a * (1 - w) + clean * w
        Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).crop((0, Y0, 1080, Y0 + 1350)).save(f)
    t = LOGO.with_suffix('.tmp.mp4')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-framerate', '30', '-i', str(fr / 'f%03d.png'), '-vf', f'tpad=stop_mode=clone:stop_duration={HOLD}',
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', str(t)], check=True)
    t.rename(LOGO)
if len(sys.argv) > 2:
    src, dst = sys.argv[1], pathlib.Path(sys.argv[2])
    d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src]))
    t = dst.with_suffix('.tmp.mp4')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-i', str(LOGO), '-filter_complex',
        f'[0:v]fps=30,format=yuv420p,setsar=1[a];[1:v]fps=30,format=yuv420p,setsar=1[b];[a][b]xfade=transition=fade:duration={XF}:offset={d - XF}[v]',
        '-map', '[v]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(t)], check=True)
    t.rename(dst); print(dst)
