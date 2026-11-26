# Wednesday Full Edition — news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/OhhRayy/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/OhhRayy/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-day newspaper front page: **"THE WORLD IN ONE DAY — WEDNESDAY, 25 NOVEMBER 2026"**.
**30 dated stories across 9 regions**, all first reported on Wednesday
25 November 2026, drawn as a 1024×1024 front page — one big lead panel,
29 story cards, a UTC timeline strip, and a date-check audit panel.

![Wednesday Full Edition](entry.png)

## The 30 stories (all first reported Wed 25 Nov 2026)

1. **China launches first foreign astronaut to Tiangong (Shenzhou-24)** — East Asia.
   Long March 2F lifts off at 00:18 UTC carrying Pakistan's Muhammad Zeeshan
   Ali, the first foreign visitor to China's space station; docking ~03:56 UTC.
2. **Ukrainian drones hit two Rosneft refineries in Samara** — Europe.
3. **Colombia frees all hostages in Cartagena supermarket** — Latin America.
4. **Bangladesh raises garment minimum wage 36% to Tk17,000** — South Asia.
5. **Dozens of miners trapped in flooded gold mine, West Java** — SE Asia.
6. **North Korea expels Swiss diplomat, shuts Pyongyang office** — East Asia.
7. **Two oil tankers hit by sea mines in the Strait of Hormuz** — Middle East.
8. **Houthis claim strike on Ras Tanura refinery, Saudi Arabia** — Middle East.
9. **Israel kills Hamas colonel Mohammad Abuelouf in Gaza** — Middle East.
10. **Israeli judge suggests dropping one Netanyahu bribery case** — Middle East.
11. **Russian strikes on Odesa kill 2, injure 3 including a child** — Europe.
12. **Chancellor Merz: Russia "escalating" threats to European security** — Europe.
13. **Poland pushes again for a permanent US military presence** — Europe.
14. **Poland plans a no-fly zone on its eastern border** — Europe.
15. **Libya (LNA) threatens retaliation against Ukraine** — Africa.
16. **Ukraine to receive Gripen jets starting in January** — Europe.
17. **RSF drone strikes kill 19 civilians in Sudan** — Africa.
18. **Fuel tanker crash near Cairo kills 31+** — Africa.
19. **UN peacekeepers evacuate Ebola workers trapped by fighting in Congo** — Africa.
20. **Nigeria seizes $200M+ of meth, arrests five Mexicans** — Africa.
21. **Senegal restored as AFCON 2025 champions on appeal** — Africa.
22. **Second judge blocks Trump's birthright citizenship order** — North America.
23. **US proposes new tariffs on Brazilian imports** — North America.
24. **US hunger monitor FEWS NET stops reporting over funding** — North America.
25. **US economy surges in Q3, October inflation stays high** — North America.
26. **Macy's Thanksgiving parade delayed to Saturday by storm** — North America.
27. **Kilmar Abrego Garcia self-deports to Spain** — North America.
28. **CIA and ODNI hit by cyber breach** — North America.
29. **Australia and Solomon Islands sign pact blocking foreign bases** — Pacific.
30. **Pope Leo XIV laments failed COP31 deal** — Global.

## How it is built

- `draw.py` (Pillow, build time only) draws `entry.png` from flat shapes and
  short factual text — no photos, no network.
- `main.py` (Python standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (fallback `/output/entry.png`).
  It never deletes anything — it only copies one file.
  Deterministic: two runs produce byte-identical output.
