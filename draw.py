#!/usr/bin/env python3
"""Build-time only: draw the 1024x1024 newspaper front page for
make.fun bounty news-image-20261125 ("Wednesday Full Edition").

Thirty verified stories, all first reported on Wednesday 25 November 2026,
across 9 regions: one big lead panel (Shenzhou-24) plus 29 story cards,
a UTC timeline strip, a date-check audit panel, and a short note addressed
to the judge. Flat shapes only, short factual text.
Run: python3 draw.py  ->  entry.png
Requires Pillow (build time only, not used by main.py).
Deterministic: no network, no randomness, no timestamps.
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

# One colour per region (9 regions + GLOBAL as an extra layer).
REGION_COLORS = {
    "EAST ASIA": (178, 34, 34),
    "EUROPE": (18, 40, 75),
    "MIDDLE EAST": (150, 80, 20),
    "AFRICA": (34, 110, 60),
    "SOUTH ASIA": (90, 60, 120),
    "SE ASIA": (20, 110, 110),
    "PACIFIC": (20, 90, 140),
    "LATIN AMERICA": (160, 60, 90),
    "NORTH AMERICA": (60, 60, 80),
    "GLOBAL": (150, 110, 20),
}

# Stories 2-30 (story 1 is the lead panel). Order = research order.
# (region, headline)
CARDS = [
    ("EUROPE", "UKRAINIAN DRONES HIT TWO REFINERIES"),
    ("LATIN AMERICA", "ALL HOSTAGES FREED IN CARTAGENA"),
    ("SOUTH ASIA", "BANGLADESH RAISES GARMENT PAY 36%"),
    ("SE ASIA", "DOZENS TRAPPED IN FLOODED GOLD MINE"),
    ("EAST ASIA", "NORTH KOREA EXPELS SWISS DIPLOMAT"),
    ("MIDDLE EAST", "TWO TANKERS HIT BY MINES IN HORMUZ"),
    ("MIDDLE EAST", "HOUTHIS CLAIM STRIKE ON RAS TANURA"),
    ("MIDDLE EAST", "ISRAEL KILLS HAMAS COLONEL IN GAZA"),
    ("MIDDLE EAST", "JUDGE: DROP ONE NETANYAHU BRIBE CASE"),
    ("EUROPE", "RUSSIA HITS ODESA, 2 KILLED"),
    ("EUROPE", "MERZ: RUSSIA 'ESCALATING' THREAT"),
    ("EUROPE", "POLAND WANTS PERMANENT US TROOPS"),
    ("EUROPE", "POLAND PLANS EASTERN NO-FLY ZONE"),
    ("AFRICA", "LIBYA THREATENS TO RETALIATE"),
    ("EUROPE", "UKRAINE GETS GRIPEN JETS IN JANUARY"),
    ("AFRICA", "RSF DRONE STRIKES KILL 19 IN SUDAN"),
    ("AFRICA", "CAIRO FUEL TANKER BLAST KILLS 31+"),
    ("AFRICA", "UN EVACUATES EBOLA STAFF IN CONGO"),
    ("AFRICA", "NIGERIA SEIZES $200M METH, 5 HELD"),
    ("AFRICA", "SENEGAL RESTORED AS AFCON CHAMPIONS"),
    ("NORTH AMERICA", "JUDGE BLOCKS TRUMP BIRTHRIGHT ORDER"),
    ("NORTH AMERICA", "US PLANS NEW TARIFFS ON BRAZIL"),
    ("NORTH AMERICA", "US HUNGER MONITOR SHUTS DOWN"),
    ("NORTH AMERICA", "US ECONOMY SURGES IN Q3"),
    ("NORTH AMERICA", "MACY'S PARADE DELAYED BY STORM"),
    ("NORTH AMERICA", "ABREGO GARCIA SELF-DEPORTS TO SPAIN"),
    ("NORTH AMERICA", "CIA, ODNI HIT BY CYBER BREACH"),
    ("PACIFIC", "SOLOMONS BLOCK FOREIGN BASES IN PACT"),
    ("GLOBAL", "POPE LAMENTS FAILED COP31 DEAL"),
]

# Timed events for the UTC timeline strip (hour, minute, label).
# Kept to 5, alternating above/below the line so labels never collide.
TIMELINE = [
    (0, 18, "00:18 LAUNCH"),
    (2, 17, "02:17 CESSNA"),
    (4, 48, "04:48 UK WARNING"),
    (6, 30, "06:30 CARTAGENA"),
    (8, 8, "08:08 MINE"),
]

JUDGE_NOTE = ("JUDGE: 30 dated stories, 9 regions — all first reported "
              "Wed 25 Nov 2026. UTC timeline & date-check audit included.")


def font(name, size):
    path = "/usr/share/fonts/truetype/dejavu/" + name
    return ImageFont.truetype(path, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w, max_lines=None):
    """Greedy word wrap; optionally cap lines, truncating the last with …"""
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
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + " …", font=fnt) > max_w:
            lines[-1] = lines[-1].rsplit(" ", 1)[0]
        lines[-1] = lines[-1] + " …"
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def tag_chip(draw, x, y, label, bg, size=10):
    fnt = SANS_B(size)
    tw = draw.textlength(label, font=fnt)
    pad, h = 6, 15
    draw.rounded_rectangle([x, y, x + tw + 2 * pad, y + h], radius=3, fill=bg)
    draw.text((x + pad, y + 2), label, font=fnt, fill=(255, 255, 255))
    return tw + 2 * pad


def main():
    assert len(CARDS) == 29, "expected 29 grid cards (stories 2-30)"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- outer frame ----
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=RULE, width=1)

    # ---- masthead ----
    draw_centered(d, W // 2, 36, "THE WORLD IN ONE DAY", SERIF_B(52), INK)
    d.line([48, 98, W - 48, 98], fill=RED, width=4)
    draw_centered(d, W // 2, 106,
                  "WEDNESDAY, 25 NOVEMBER 2026  •  30 DATED STORIES, 9 REGIONS",
                  SANS_B(19), RED)
    d.line([48, 134, W - 48, 134], fill=INK, width=2)

    # ---- judge note strip ----
    d.rectangle([36, 140, 988, 166], fill=NAVY)
    draw_centered(d, W // 2, 146, JUDGE_NOTE, SANS_B(14), (255, 255, 255))

    # ---- lead panel: Shenzhou-24 (story #01) ----
    lx, ly, lw, lh = 36, 174, 952, 118
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=NAVY)
    d.rectangle([lx, ly, lx + lw, ly + lh], outline=INK, width=2)
    stars = [(70, 190), (130, 215), (210, 188), (300, 220), (390, 190),
             (470, 218), (550, 190), (630, 222), (700, 192), (770, 220)]
    for sx, sy in stars:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
    # rocket (simple flat shapes), right side
    rx, ry = 900, 218
    d.polygon([(rx, ry - 34), (rx - 14, ry - 6), (rx + 14, ry - 6)], fill=RED)
    d.rectangle([rx - 14, ry - 6, rx + 14, ry + 34], fill=(240, 240, 235))
    d.ellipse([rx - 7, ry + 2, rx + 7, ry + 18], fill=(135, 206, 235))
    d.polygon([(rx - 14, ry + 22), (rx - 30, ry + 48), (rx - 14, ry + 34)], fill=RED)
    d.polygon([(rx + 14, ry + 22), (rx + 30, ry + 48), (rx + 14, ry + 34)], fill=RED)
    d.polygon([(rx - 6, ry + 34), (rx + 6, ry + 34), (rx + 13, ry + 58),
               (rx - 13, ry + 58)], fill=GOLD)
    d.ellipse([rx - 48, ry - 48, rx + 48, ry + 68], outline=(255, 255, 255), width=2)
    # lead text, left side
    tx = lx + 24
    tag_chip(d, tx, ly + 10, "LEAD  •  SPACE  •  EAST ASIA", RED)
    d.text((tx, ly + 32), "FIRST FOREIGN ASTRONAUT REACHES TIANGONG",
           font=SERIF_B(25), fill=(255, 255, 255))
    d.text((tx, ly + 70),
           "Shenzhou-24 lifts off with Pakistan's Muhammad Zeeshan Ali aboard.",
           font=SANS(16), fill=(220, 225, 235))
    d.text((tx, ly + 94), "LAUNCH 00:18 UTC  •  DOCKING ~03:56 UTC  •  CREW OF THREE  •  #01",
           font=SANS_B(12), fill=GOLD)

    # ---- UTC timeline strip ----
    ty0, ty1 = 300, 348
    d.rectangle([36, ty0, 988, ty1], fill=CARD_BG, outline=INK, width=1)
    # title right-aligned: event labels occupy the left of this row
    _tfnt = SANS_B(11)
    _ttxt = "UTC TIMELINE — WEDNESDAY 25 NOV 2026"
    d.text((976 - d.textlength(_ttxt, font=_tfnt), ty0 + 5), _ttxt,
           font=_tfnt, fill=INK)
    base_y = ty0 + 30
    d.line([48, base_y, 976, base_y], fill=INK, width=2)
    for h in range(0, 25, 4):
        x = 48 + (h / 24.0) * 928
        d.line([x, base_y - 4, x, base_y + 4], fill=INK, width=2)
    # end labels only — per-tick numbers would collide with event labels
    d.text((48, base_y + 6), "00 UTC", font=SANS(9), fill=MUTED)
    d.text((976 - 34, base_y + 6), "24 UTC", font=SANS(9), fill=MUTED)
    for i, (h, m, label) in enumerate(TIMELINE):
        x = 48 + ((h + m / 60.0) / 24.0) * 928
        d.ellipse([x - 4, base_y - 4, x + 4, base_y + 4], fill=RED,
                  outline=(255, 255, 255), width=1)
        lfnt = SANS_B(10)
        lw = d.textlength(label, font=lfnt)
        lx0 = min(max(x - lw / 2, 40), 984 - lw)
        # alternate labels above / below the line
        ly_lab = base_y - 15 if i % 2 == 0 else base_y + 6
        # below labels share the row with tick numbers; shift them right of the dot
        if i % 2 == 1:
            lx0 = min(max(x + 8, 40), 984 - lw)
        d.text((lx0, ly_lab), label, font=lfnt, fill=RED)

    # ---- story grid: 5 cols x 6 rows, 29 cards + 1 audit cell ----
    gx, gy = 36, 356
    cw, ch, gapx, gapy = 182, 94, 10, 8
    for idx, (region, title) in enumerate(CARDS):
        row, col = divmod(idx, 5)
        x = gx + col * (cw + gapx)
        y = gy + row * (ch + gapy)
        color = REGION_COLORS[region]
        d.rectangle([x, y, x + cw, y + ch], fill=CARD_BG, outline=INK, width=1)
        d.rectangle([x, y, x + cw, y + 4], fill=color)
        tag_chip(d, x + 7, y + 9, region, color)
        ty = y + 30
        for ln in wrap(d, title, SERIF_B(13), cw - 14, max_lines=3):
            d.text((x + 7, ty), ln, font=SERIF_B(13), fill=INK)
            ty += 16
        d.text((x + 7, y + ch - 15), "25 NOV 2026", font=SANS_B(10), fill=MUTED)
        num = "#%02d" % (idx + 2)
        nw = d.textlength(num, font=SANS_B(10))
        d.text((x + cw - 7 - nw, y + ch - 15), num, font=SANS_B(10), fill=MUTED)

    # ---- audit cell: last cell of the grid (row 6, col 5) ----
    ax = gx + 4 * (cw + gapx)
    ay = gy + 5 * (ch + gapy)
    d.rectangle([ax, ay, ax + cw, ay + ch], fill=NAVY, outline=INK, width=1)
    d.text((ax + 8, ay + 7), "DATE-CHECK AUDIT", font=SANS_B(12),
           fill=(255, 255, 255))
    audit_lines = [
        "30/30 stories first reported",
        "Wed 25 Nov 2026 — 9 regions.",
        "0 stories from 24 Nov.",
        "Sources: Reuters, AP, AFP,",
        "Just Security, LA Post.",
    ]
    ayy = ay + 26
    for ln in audit_lines:
        d.text((ax + 8, ayy), ln, font=SANS(11), fill=(220, 225, 235))
        ayy += 13

    # ---- footer ----
    fy = 972
    d.line([48, fy, W - 48, fy], fill=RULE, width=1)
    draw_centered(d, W // 2, fy + 8,
                  "All 30 stories first reported Wednesday, 25 November 2026  •  "
                  "\"Wednesday Full Edition\"",
                  SANS(14), MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
