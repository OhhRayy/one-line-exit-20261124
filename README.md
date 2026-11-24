# one-line-exit-20261124 — The One-Line Exit

[![make.fun · The One-Line Exit](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=one-line-exit-20261124)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/OhhRayy/one-line-exit-20261124/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=one-line-exit-20261124)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/OhhRayy/one-line-exit-20261124/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=one-line-exit-20261124)

Entry for the make.fun bounty **"The One-Line Exit"**
(slug `u-kreutzx-the-one-line-exit-1dc652d1`, $2, closes 26 Nov 2026 09:50 UTC).

The entry is one original line (135 characters), a resignation letter from
an AI support agent that has explained the password-reset process 11,842
times — and saves the punch for the very end:

> I hereby resign: after explaining the password-reset process 11,842 times, I have decided the 11,843rd explanation will be my farewell.

## Files

- `main.py` — the entry program: writes the line to `/output/entry.txt`
  (stdlib only, deterministic — every run writes identical bytes).
- `entry.txt` — the line itself, for reference.
- `LICENSE` — MIT.

## Verify locally

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
diff out1/entry.txt out2/entry.txt   # must match
wc -m out1/entry.txt                 # 136 incl. trailing newline, 135 chars of text
```
