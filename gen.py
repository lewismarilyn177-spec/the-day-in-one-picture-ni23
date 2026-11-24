#!/usr/bin/env python3
"""THE DAY IN ONE PICTURE — 23 November 2026.
One dominant hero (Benghazi corvette sinking) + 3 icon cards + ticker.
Deterministic: pure PIL, no network, no random, fixed fonts."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (244, 236, 216)
INK = (20, 34, 52)
RED = (196, 40, 28)
GOLD = (218, 168, 60)
SEA = (26, 42, 62)
SEALIGHT = (52, 74, 100)
CREAMDIM = (233, 222, 196)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = F + "DejaVuSerif-Bold.ttf"
SERIF = F + "DejaVuSerif.ttf"
SANS_B = F + "DejaVuSans-Bold.ttf"
SANS = F + "DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def text_c(x, y, s, f, fill, anchor="mm", ls=None):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor, align="left")

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 8], fill=RED)
f_kick = font(SANS_B, 21)
f_date = font(SERIF_B, 64)
f_deck = font(SERIF, 19)
d.text((W/2, 44), "THE WORLD IN ONE PICTURE  ·  MONDAY", font=f_kick, fill=RED, anchor="mm")
d.text((W/2, 108), "23 NOVEMBER 2026", font=f_date, fill=INK, anchor="mm")
# deck line with interpuncts
deck = "Ukraine sinks Russian corvette at Benghazi  ·  EU’s 22nd sanctions  ·  COP31 ends with no deal"
d.text((W/2, 178), deck, font=f_deck, fill=INK, anchor="mm")
d.line([48, 216, W-48, 216], fill=INK, width=3)

# ---------------- HERO: Benghazi night raid (y 232..712) ----------------
hy0, hy1 = 228, 716
d.rectangle([0, hy0, W, hy1], fill=SEA)
# stars (fixed positions)
for sx, sy, r in [(70,262,2),(150,300,1),(230,268,2),(330,296,1),(430,258,2),(540,290,1),
                  (640,262,2),(760,300,1),(860,268,2),(940,296,2),(500,320,1),(280,330,1)]:
    d.ellipse([sx-r, sy-r, sx+r, sy+r], fill=(226,230,238))
# moon
d.ellipse([872, 246, 936, 310], fill=(238,232,212))
d.ellipse([858, 252, 918, 312], fill=SEA)  # crescent cut
# distant skyline (Benghazi port), dim buildings above horizon
horizon = hy1 - 168
bx = 24
for w, hgt in [(54,64),(38,92),(64,56),(46,110),(70,70),(40,88),(58,120),(36,66),(62,94),
               (48,58),(70,102),(44,76),(66,88),(38,112),(58,62),(46,96),(64,72)]:
    d.rectangle([bx, horizon-hgt, bx+w, horizon], fill=(30,44,64))
    # a few lit windows
    if (bx // 7) % 3 == 0:
        for wy in range(horizon-hgt+10, horizon-8, 18):
            wx = bx + 6 + ((bx + wy) % max(w-14, 4))
            d.rectangle([wx, wy, wx+5, wy+6], fill=(216,178,96))
    bx += w + 6
d.rectangle([0, horizon, W, hy1], fill=(18,30,46))  # water
# hull reflections
for rx in range(30, W, 90):
    d.line([rx, hy1-40, rx+26, hy1-40], fill=(40,58,80), width=3)

# the corvette: listing, burning, at right-center
ship_cx, ship_y = 620, hy1-190
# hull (tilted, bow at left)
d.polygon([(ship_cx-190, ship_y+30),(ship_cx+150, ship_y+16),(ship_cx+168, ship_y+46),
           (ship_cx-180, ship_y+62)], fill=(10,16,26))
d.line([ship_cx+150, ship_y+16, ship_cx+196, ship_y+34], fill=(226,230,238), width=4)
# superstructure (blocks toward stern, right side)
d.rectangle([ship_cx+30, ship_y-14, ship_cx+120, ship_y+20], fill=(16,24,36))
d.rectangle([ship_cx+50, ship_y-44, ship_cx+108, ship_y-10], fill=(20,30,44))
d.rectangle([ship_cx+66, ship_y-70, ship_cx+96, ship_y-40], fill=(24,36,50))
# lit bridge windows
for wx in range(ship_cx+56, ship_cx+104, 14):
    d.rectangle([wx, ship_y-38, wx+8, ship_y-30], fill=(216,178,96))
# mast
d.line([ship_cx+80, ship_y-70, ship_cx+80, ship_y-108], fill=(20,30,44), width=5)
d.ellipse([ship_cx+72, ship_y-114, ship_cx+88, ship_y-98], fill=(24,36,50))
# flames pouring from midships hole
fl = [(ship_cx-40, ship_y+18, 30, (232,120,32)), (ship_cx-30, ship_y+10, 22, (240,168,64)),
      (ship_cx-36, ship_y+24, 16, (246,208,120)), (ship_cx-90, ship_y+26, 20, (232,120,32)),
      (ship_cx-84, ship_y+20, 13, (240,168,64)), (ship_cx+4, ship_y+22, 18, (232,120,32))]
for fx, fy, fr, c in fl:
    d.ellipse([fx-fr, fy-fr, fx+fr, fy+fr], fill=c)
# smoke column rising from midships
for i, (mx, mw, mc) in enumerate([(ship_cx-38, 30, (70,74,84)),(ship_cx-50, 40, (84,88,96)),
                                  (ship_cx-28, 46, (98,102,110)),(ship_cx-46, 54, (112,116,124))]):
    sy = ship_y-70 - i*46
    d.ellipse([mx-mw, sy-mw//2, mx+mw, sy+mw//2], fill=mc)
# naval drones attacking from left: wake lines + small dark hulls
for (dx, dy) in [(130, hy1-70), (260, hy1-88), (60, hy1-56)]:
    d.line([dx-60, dy+8, dx+90, dy-4], fill=(150,160,178), width=3)
    d.line([dx-58, dy+18, dx+60, dy+10], fill=(110,122,142), width=2)
    d.ellipse([dx+88, dy-14, dx+124, dy+2], fill=(10,16,26))
    d.rectangle([dx+112, dy-10, dx+130, dy-6], fill=(200,90,40))  # hot exhaust
# red tracer lines from drones to ship
for (tx, ty) in [(300, hy1-96), (170, hy1-86)]:
    d.line([tx, ty, ship_cx-60, ship_y+8], fill=(214,60,40), width=3)
d.text((54, hy1-56), "UKRAINIAN NAVAL DRONES →", font=font(SANS_B, 20), fill=(226,230,238), anchor="lm")

# hero caption block
d.rectangle([0, hy1-64, W, hy1], fill=(12,20,32))
d.text((W/2, hy1-40), "BENGHAZI  —  CORVETTE “MERKURY” SUNK", font=font(SERIF_B, 34), fill=(240,234,220), anchor="mm")
d.text((30, hy0+18), "LIBYA  ·  AP · AL JAZEERA · GUARDIAN  ·  NOV 23", font=font(SANS_B, 15), fill=(160,174,194), anchor="la")

# ---------------- secondary: 3 icon cards (y 740..928) ----------------
cy0, cy1 = 736, 930
cw = (W - 4*28) // 3
xs = [28, 28 + cw + 28, 28 + 2*(cw + 28)]
f_head = font(SANS_B, 21)
f_sub  = font(SANS, 15)

cards = [
    ("EU 22ND SANCTIONS", "ON RUSSIA", "banks, crypto, sports ban"),
    ("IRAN VS BLOCKADE", "“ALL AVAILABLE MEANS”", "Houthis hit Saudi refinery"),
    ("COP31: NO DEAL", "SUMMIT ENDS EMPTY", "Guterres “deeply disappointed”"),
]

for i, ((t1, t2, sub), x) in enumerate(zip(cards, xs)):
    d.rectangle([x, cy0, x+cw, cy1-4], fill=(255,250,238), outline=INK, width=3)
    # icon zone
    ix, iy = x + cw//2, cy0 + 58
    if i == 0:   # 12 gold stars over crossed-out Russian tricolor
        for k in range(12):
            ang = k * 30
            import math
            sx = ix + 44*math.cos(math.radians(ang)); sy = iy + 44*math.sin(math.radians(ang))
            d.ellipse([sx-7, sy-7, sx+7, sy+7], fill=GOLD)
        for yy, cc in [(0, (232,236,240)), (16, (70,100,150)), (32, (200,60,44))]:
            d.rectangle([ix-52, iy+yy-8, ix+52, iy+yy+8], fill=cc)
        d.line([ix-58, iy-14, ix+58, iy+44], fill=RED, width=10)
    elif i == 1:  # tanker ship + flame + lock
        d.rectangle([ix-60, iy+6, ix+60, iy+26], fill=(40,58,80))
        d.rectangle([ix-20, iy-16, ix+22, iy+6], fill=(60,80,104))
        d.ellipse([ix+34, iy-22, ix+62, iy+6], fill=(232,120,32))
        d.ellipse([ix+42, iy-14, ix+56, iy+0], fill=(246,208,120))
        d.ellipse([ix-58, iy-10, ix-26, iy+18], fill=RED)
        d.rectangle([ix-46, iy+0, ix-38, iy+10], fill=(255,250,238))
        d.rectangle([ix-34, iy-4, ix-26, iy+6], fill=(255,250,238))
    else:         # globe with a hollow gavel / broken handshake
        d.ellipse([ix-44, iy-44, ix+44, iy+44], outline=INK, width=6)
        d.ellipse([ix-44, iy-16, ix+44, iy+16], outline=INK, width=4)
        d.line([ix, iy-44, ix, iy+44], fill=INK, width=4)
        d.line([ix-44, iy+8, ix+44, iy+8], fill=(200,60,44), width=8)
        d.text((ix+64, iy), "×", font=font(SANS_B, 40), fill=RED, anchor="lm")
    d.text((x+16, cy0+118), t1, font=f_head, fill=RED, anchor="la")
    d.text((x+16, cy0+146), t2, font=f_head, fill=INK, anchor="la")
    d.text((x+16, cy0+166), sub, font=f_sub, fill=(90,96,108), anchor="la")

# ---------------- ticker (y 950..1024) ----------------
d.rectangle([0, 950, W, 1024], fill=INK)
f_tick = font(SANS_B, 21)
f_tag  = font(SANS_B, 15)
d.text((24, 966), "ALSO", font=f_tag, fill=GOLD, anchor="la")
ticks = [
    "ICJ: MYANMAR GUILTY OF ROHINGYA GENOCIDE",
    "INDIA PLEDGES $1.6BN TO NEPAL",
    "NATO: RUSSIA NUCLEAR SATELLITE WARNING",
    "US DEMS: BIGGEST HOUSE WIN SINCE 1992",
]
yy = 992
d.text((24, yy), ticks[0], font=f_tick, fill=(238,232,220), anchor="lm")
d.text((24, yy+24), " · ".join(ticks[1:3]), font=font(SANS_B, 17), fill=(200,206,216), anchor="lm")
d.text((24, yy+46), ticks[3] + "  ·  VESSEL ATTACKS GULF OF FINLAND", font=font(SANS_B, 17), fill=(200,206,216), anchor="lm")

# footer date check
d.rectangle([0, 1016, W, 1024], fill=RED)

import os
os.makedirs("/root/makefun/ni23-rescue/repo", exist_ok=True)
img.save("/root/makefun/ni23-rescue/repo/entry.png", "PNG", optimize=True)
print("saved", os.path.getsize("/root/makefun/ni23-rescue/repo/entry.png"), "bytes")
