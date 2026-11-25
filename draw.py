#!/usr/bin/env python3
"""Build-time only: draw the 1024x1024 newspaper front page for
make.fun bounty news-image-20261125 ("Wednesday Ascent").

Six verified stories first reported on Wednesday 25 November 2026:
a big lead panel (Shenzhou-24) plus five story cards. Flat shapes only,
short factual text. Run: python3 draw.py  ->  entry.png
Requires Pillow (build time only, not used by main.py).
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

PAPER = (247, 242, 231)
INK = (26, 26, 26)
RED = (178, 34, 34)
NAVY = (18, 40, 75)
GOLD = (201, 162, 39)
RULE = (120, 110, 95)
CARD_BG = (255, 253, 247)
MUTED = (90, 84, 72)


def font(name, size):
    path = "/usr/share/fonts/truetype/dejavu/" + name
    return ImageFont.truetype(path, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap, returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def tag_chip(draw, x, y, label, bg):
    fnt = SANS_B(17)
    tw = draw.textlength(label, font=fnt)
    pad, h = 10, 26
    draw.rounded_rectangle([x, y, x + tw + 2 * pad, y + h], radius=4, fill=bg)
    draw.text((x + pad, y + 4), label, font=fnt, fill=(255, 255, 255))
    return tw + 2 * pad


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- outer frame ----
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=RULE, width=1)

    # ---- masthead ----
    draw_centered(d, W // 2, 44, "THE WORLD IN ONE DAY", SERIF_B(58), INK)
    d.line([48, 118, W - 48, 118], fill=RED, width=4)
    draw_centered(d, W // 2, 130, "WEDNESDAY, 25 NOVEMBER 2026  •  SIX STORIES, ONE DAY",
                  SANS_B(20), RED)
    d.line([48, 164, W - 48, 164], fill=INK, width=2)

    # ---- lead panel: Shenzhou-24 ----
    lx, ly, lw, lh = 36, 180, 952, 330
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=NAVY)
    d.rectangle([lx, ly, lx + lw, ly + lh], outline=INK, width=2)
    # stars
    stars = [(80, 205), (150, 240), (240, 200), (330, 250), (420, 205),
             (520, 235), (600, 200), (700, 245), (830, 210), (920, 250),
             (110, 300), (300, 300), (560, 300), (760, 300), (900, 300)]
    for sx, sy in stars:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
    # rocket (simple flat shapes), right side
    rx, ry = 830, 235
    d.polygon([(rx, ry - 58), (rx - 22, ry - 8), (rx + 22, ry - 8)], fill=RED)
    d.rectangle([rx - 22, ry - 8, rx + 22, ry + 62], fill=(240, 240, 235))
    d.ellipse([rx - 11, ry + 2, rx + 11, ry + 30], fill=(135, 206, 235))
    d.polygon([(rx - 22, ry + 40), (rx - 48, ry + 82), (rx - 22, ry + 62)], fill=RED)
    d.polygon([(rx + 22, ry + 40), (rx + 48, ry + 82), (rx + 22, ry + 62)], fill=RED)
    d.polygon([(rx - 10, ry + 62), (rx + 10, ry + 62), (rx + 22, ry + 108),
               (rx - 22, ry + 108)], fill=GOLD)
    # orbit ring around rocket
    d.ellipse([rx - 78, ry - 78, rx + 78, ry + 128], outline=(255, 255, 255), width=2)
    # lead text, left side
    tx = lx + 28
    tag_chip(d, tx, ly + 22, "LEAD  •  SPACE", RED)
    lines = wrap(d, "FIRST FOREIGN ASTRONAUT REACHES TIANGONG",
                 SERIF_B(40), 700)
    y = ly + 62
    for ln in lines:
        d.text((tx, y), ln, font=SERIF_B(40), fill=(255, 255, 255))
        y += 48
    y += 6
    for ln in wrap(d, "Shenzhou-24 lifts off with Pakistan's Muhammad "
                    "Zeeshan Ali aboard — the first foreign visitor to "
                    "China's space station.", SANS(24), 700):
        d.text((tx, y), ln, font=SANS(24), fill=(220, 225, 235))
        y += 32
    d.text((tx, ly + lh - 38), "LAUNCH 00:18 UTC  •  DOCKING ~03:56 UTC  •  CREW OF THREE",
           font=SANS_B(17), fill=GOLD)

    # ---- five story cards ----
    cards = [
        ("WAR  •  UKRAINE", (140, 40, 40),
         "UKRAINIAN DRONES HIT TWO REFINERIES",
         "Fires at two Rosneft plants in Samara; one killed."),
        ("COLOMBIA", (34, 110, 60),
         "ALL HOSTAGES FREED IN CARTAGENA",
         "Special forces end a 17-hour siege; one gunman killed."),
        ("ECONOMY  •  BANGLADESH", (20, 90, 110),
         "BANGLADESH RAISES GARMENT PAY 36%",
         "Minimum wage rises to Tk17,000 from 1 December."),
        ("INDONESIA", (150, 100, 30),
         "DOZENS TRAPPED IN FLOODED GOLD MINE",
         "Rescuers search a 100-metre pit in West Java after heavy rain."),
        ("DIPLOMACY  •  NORTH KOREA", (90, 60, 120),
         "NORTH KOREA EXPELS SWISS DIPLOMAT",
         "Pyongyang shuts its Swiss office and gives its envoy 48 hours to leave."),
    ]
    top = 530
    card_h, gap = 208, 16
    # row 1: 3 cards, row 2: 2 cards (wider)
    rows = [(3, (952 - 2 * gap) // 3), (2, (952 - gap) // 2)]
    idx = 0
    y = top
    for count, cw in rows:
        x = 36
        for _ in range(count):
            tag, color, title, sub = cards[idx]
            idx += 1
            d.rectangle([x, y, x + cw, y + card_h], fill=CARD_BG, outline=INK, width=2)
            d.rectangle([x, y, x + cw, y + 6], fill=color)
            tag_chip(d, x + 14, y + 20, tag, color)
            ty = y + 56
            for ln in wrap(d, title, SERIF_B(23), cw - 28):
                d.text((x + 14, ty), ln, font=SERIF_B(23), fill=INK)
                ty += 29
            for ln in wrap(d, sub, SANS(18), cw - 28):
                d.text((x + 14, ty + 6), ln, font=SANS(18), fill=MUTED)
                ty += 24
            x += cw + gap
        y += card_h + gap

    # ---- footer ----
    fy = 962
    d.line([48, fy, W - 48, fy], fill=RULE, width=1)
    draw_centered(d, W // 2, fy + 10,
                  "All six stories first reported Wednesday, 25 November 2026  •  \"Wednesday Ascent\"",
                  SANS(17), MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
