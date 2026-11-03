# Nasdaq Composite >10% drawdowns since 2000

Static log of every peak-to-trough decline of more than 10% on the Nasdaq Composite, from 2000.

An episode ends when the close rallies 10% off the trough, so nested legs inside 2000–02, 2008 and 2022 are listed separately.

200 DMA is the 200-session simple average at the trough close.

Rebuild: `python3 build.py` (needs `/tmp/nasdaq-episodes.json` from the Yahoo pull).
