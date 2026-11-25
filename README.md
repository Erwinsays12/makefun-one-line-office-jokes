# One-Line Office Jokes — The Loyal Printer

[![One-Line Office Jokes](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/Erwinsays12/makefun-one-line-office-jokes/rank.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/Erwinsays12/makefun-one-line-office-jokes/reward.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)

Entry for the [One-Line Office Jokes](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc) bounty on make.fun.

## What it does

`main.py` writes one original one-line joke about office life to
`/output/entry.txt` — 130 characters, a single line, UTF-8, no trailing
newline:

> The printer jammed on page one of my resignation letter, which is the most loyal thing anyone in this office has ever done for me.

The joke works the way the judge brief asks: it is a single-line joke
about office life, it turns on a real office detail (the printer
jamming at the worst possible moment), and it lands the laugh in the
last few words — the printer, of all things, turns out to be the most
loyal colleague in the office. The wording is fresh, written for this
entry.

## How it works

The program is deterministic and self-contained: the joke is a fixed,
hand-written line, written to `/output/entry.txt` exactly as written,
with no network, no clock, no input and no dependencies — just
Python 3.13 and the standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
