#!/usr/bin/env python3
"""Generate og.png — the social card, drawn in the site's own design language."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
PAPER = (244, 241, 233)
PANEL = (237, 234, 222)
INK = (38, 37, 31)
DIM = (125, 122, 109)
ACCENT = (194, 53, 31)
LINE = (219, 215, 199)
LINE_S = (185, 180, 160)

F = "/home/d0mi3/Z/payloadcraft/static/fonts/"
serif = F + "fraunces-var.woff2"
mono400 = F + "plexmono-400.woff2"
mono600 = F + "plexmono-600.woff2"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# blueprint grid, faint
for x in range(0, W, 120):
    d.line([(x, 0), (x, H)], fill=(38, 37, 31, 10), width=1)
for y in range(0, H, 120):
    d.line([(0, y), (W, y)], fill=(38, 37, 31, 10), width=1)

# registration marks, corners
def regmark(cx, cy):
    r = 13
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=DIM, width=2)
    d.line([(cx, cy - 20), (cx, cy + 20)], fill=DIM, width=2)
    d.line([(cx - 20, cy), (cx + 20, cy)], fill=DIM, width=2)

regmark(46, 46)
regmark(W - 46, H - 46)

# header rule + masthead text
d.line([(60, 120), (W - 60, 120)], fill=INK, width=3)
m600 = font(mono600, 24)
m400s = font(mono400, 20)
m400k = font(mono400, 17)
d.text((60, 66), "PAYLOADCRAFT", font=m600, fill=INK)
d.text((62, 96), "OFFENSIVE SECURITY · FIELD NOTES", font=font(mono400, 13), fill=DIM)
# doc block, right
d.text((W - 60 - 330, 66), "DOC FM-PC-26 · REV 10·26", font=font(mono400, 15), fill=INK)
d.text((W - 60 - 330, 90), "CLASS UNCLASS · EDU", font=font(mono400, 15), fill=DIM)

# headline — Fraunces, with red italic emphasis
fr = font(serif, 92)
d.text((60, 190), "Reproduce it,", font=fr, fill=INK)
d.text((60, 296), "or it didn’t", font=fr, fill=ACCENT)
d.text((60, 402), "happen.", font=fr, fill=INK)

# right-side spec sheet panel
px, py, pw, ph = W - 460, 170, 400, 330
d.rectangle([px + 10, py + 10, px + pw + 10, py + ph + 10], fill=(38, 37, 31, 18))
d.rectangle([px, py, px + pw, py + ph], fill=PANEL, outline=LINE_S, width=2)
d.line([(px, py + 54), (px + pw, py + 54)], fill=LINE_S, width=2)
d.text((px + 20, py + 16), "SPEC / STATUS", font=font(mono600, 15), fill=INK)
d.ellipse([px + pw - 34, py + 20, px + pw - 20, py + 34], fill=ACCENT)

rows = [
    ("ENTRIES ON FILE", "IN PREP"),
    ("FEED", "RSS 2.0 FULL-TEXT"),
    ("TRACKERS", "NONE DETECTED"),
]
yy = py + 76
for k, v in rows:
    d.text((px + 20, yy), k, font=m400k, fill=DIM)
    d.text((px + 20, yy + 22), v, font=font(mono600, 18), fill=INK)
    yy += 66
    if yy < py + ph - 60:
        for i in range(0, pw - 40, 14):
            d.line([(px + 20 + i, yy - 12), (px + 20 + i + 7, yy - 12)], fill=LINE, width=1)

# motto
d.text((px + 20, py + ph - 78), "“ if it can’t be reproduced,", font=font(serif, 24), fill=INK)
d.text((px + 20, py + ph - 44), "it’s a story — not a writeup. ”", font=font(serif, 24), fill=INK)

# footer rule
d.line([(60, H - 90), (W - 60, H - 90)], fill=INK, width=3)
d.text((60, H - 66), "NO TRACKERS · NO JS · RSS ONLY", font=font(mono400, 14), fill=DIM)
d.text((W - 60 - 220, H - 66), "PAYLOADCRAFT.COM", font=m600, fill=INK)

# barcode strip under headline
bx, by = 60, 520
xx = bx
import random
random.seed(26)
while xx < bx + 300:
    w = random.choice([2, 2, 3, 5])
    d.rectangle([xx, by, xx + w, by + 40], fill=INK)
    xx += w + random.choice([3, 4, 6, 8])
d.text((bx, by + 48), "PN·2026·PC", font=font(mono400, 13), fill=DIM)

img.save("/home/d0mi3/Z/payloadcraft/static/og.png", optimize=True)
print("og.png written", img.size)
