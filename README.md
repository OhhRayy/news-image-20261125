# Wednesday Ascent — news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/OhhRayy/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/OhhRayy/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-day newspaper front page: **"THE WORLD IN ONE DAY — WEDNESDAY, 25 NOVEMBER 2026"**.
Six stories, all first reported on Wednesday 25 November 2026, drawn as a
1024×1024 front page — one big lead panel plus five story cards.

![Wednesday Ascent](entry.png)

## The six stories

1. **China launches first foreign astronaut to Tiangong (Shenzhou-24)** — Long March 2F
   lifts off from Jiuquan at 00:18 UTC carrying Tang Hongbo, Wu Yi, and
   Pakistan's Muhammad Zeeshan Ali, the first foreign visitor to China's
   space station; docking ~03:56 UTC.
2. **Ukrainian drones hit two Rosneft refineries in Samara** — Syzran and Kuibyshev
   plants catch fire overnight; one person killed.
3. **Colombia frees all hostages in Cartagena supermarket** — special forces end a
   ~17-hour siege at an Éxito store; one gunman killed, four detained.
4. **Bangladesh raises garment minimum wage 36% to Tk17,000** — decided after a
   ~12-hour wage-board vote; effective 1 December.
5. **Dozens of miners trapped in flooded gold mine, West Java** — rescuers search a
   100-metre pit after heavy rain floods the illegal mine.
6. **North Korea expels Swiss diplomat, shuts Pyongyang office** — KCNA announces the
   Swiss envoy persona non grata with 48 hours to leave.

## How it is built

- `draw.py` (Pillow, build time only) draws `entry.png` from flat shapes and
  short factual text — no photos, no network.
- `main.py` (Python standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (fallback `/output/entry.png`).
  Deterministic: two runs produce byte-identical output.
