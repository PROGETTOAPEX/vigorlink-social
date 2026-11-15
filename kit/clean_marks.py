"""Remove numbered orange badges from guide screenshots (frames stay as highlights)."""
import sys, cv2, numpy as np, pathlib
src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
im = cv2.imread(str(src)); hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
# badge orange #F97316 -> hue ~ 12 (opencv 0-180), high sat/val
m = cv2.inRange(hsv, (5, 170, 200), (20, 255, 255))
blob = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))   # fill the white digit
blob = cv2.morphologyEx(blob, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
n, lab, st, _ = cv2.connectedComponentsWithStats(blob)
mask = np.zeros_like(m)
for i in range(1, n):
    x, y, w, h, a = st[i]
    if 25 <= w <= 80 and 25 <= h <= 80 and 0.6 < w / h < 1.6:
        cv2.circle(mask, (x + w // 2, y + h // 2), int(max(w, h) / 2 + 7), 255, -1)
out = cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
cv2.imwrite(str(dst), out); print(dst.name, int((mask > 0).sum() / 1000), 'k px cleaned')
