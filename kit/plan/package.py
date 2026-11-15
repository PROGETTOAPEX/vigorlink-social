"""Packs rendered posts for publishing: Reels get the VigorLink sound (signature A), carousels become JPG.
Output in /home/claude/vigorlink-social/plan/. Prints the ids packed in this run."""
import json, os, subprocess, sys
from PIL import Image
sys.path.insert(0, 'audio')
KIT = '/home/claude/social/kit'; DST = '/home/claude/vigorlink-social/plan'
os.makedirs(DST, exist_ok=True)
cal = json.load(open(f'{KIT}/plan/calendar.json'))
done = []
rendered = set()
for w in 'ab':
    lp = f'{KIT}/plan/render_{w}.log'
    if os.path.exists(lp):
        rendered |= {l.split()[1] for l in open(lp) if l.startswith('done ')}
for p in cal:
    out = f"{KIT}/out/{p['id']}"
    marker = f"{DST}/{p['id']}.ok"
    if os.path.exists(marker) or p['id'] not in rendered: continue
    if p['format'] == 'reel':
        v = f"{out}/reel.mp4"
        if not os.path.exists(v) or os.path.exists(f"{out}/_frames"): continue
        d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', v]))
        wav = f"{KIT}/audio/plan_{p['id']}.wav"
        subprocess.check_call(['python3', f'{KIT}/audio/brand.py', str(d), wav, 'A'])
        subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-i', v, '-i', wav, '-filter_complex', '[1:a]volume=0.6[a]', '-map', '0:v', '-map', '[a]',
                               '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', f"{DST}/{p['id']}.mp4"])
        os.remove(wav)
        Image.open(f"{out}/tt_01.png").convert('RGB').save(f"{DST}/{p['id']}.jpg", quality=90)
    else:
        n = p['slides']
        if not all(os.path.exists(f"{out}/ig_{i:02d}.png") for i in range(1, n + 1)): continue
        # only when the reel-less post is fully rendered (tt files are written after ig)
        if not os.path.exists(f"{out}/tt_{n:02d}.png"): continue
        for i in range(1, n + 1):
            Image.open(f"{out}/ig_{i:02d}.png").convert('RGB').save(f"{DST}/{p['id']}_{i:02d}.jpg", quality=90)
    open(marker, 'w').write('ok'); done.append(p['id'])
print(len(done), ' '.join(done))
