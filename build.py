#!/usr/bin/env python3
"""Bake Nasdaq Composite >10% drawdown episodes into data.js."""
import json
from datetime import date

eps = json.load(open("/tmp/nasdaq-episodes.json"))
weekly = json.load(open("/tmp/nasdaq-weekly.json"))
meta = json.load(open("/tmp/nasdaq-meta.json"))

# CPI-U YoY, BLS, trough month (percent)
CPI = {
    (2000, 3): 3.8, (2000, 4): 3.1, (2000, 5): 3.2, (2000, 7): 3.7, (2000, 8): 3.4,
    (2000, 9): 3.5, (2000, 10): 3.4, (2000, 11): 3.4, (2000, 12): 3.4,
    (2001, 1): 3.7, (2001, 4): 3.3, (2001, 5): 3.6, (2001, 9): 2.6,
    (2002, 1): 1.1, (2002, 2): 1.1, (2002, 3): 1.5, (2002, 5): 1.2, (2002, 8): 1.8, (2002, 10): 2.0, (2002, 11): 2.2,
    (2003, 3): 3.0,
    (2004, 1): 1.9, (2004, 8): 2.7, (2004, 12): 3.3,
    (2005, 4): 3.5,
    (2006, 4): 3.5, (2006, 7): 4.1,
    (2007, 10): 3.5,
    (2008, 3): 4.0, (2008, 6): 5.0, (2008, 7): 5.6, (2008, 8): 5.4, (2008, 10): 3.7, (2008, 11): 1.1,
    (2009, 1): 0.0, (2009, 2): 0.2, (2009, 3): -0.4,
    (2010, 4): 2.2, (2010, 7): 1.2,
    (2011, 4): 3.2, (2011, 8): 3.8, (2011, 9): 3.9, (2011, 10): 3.5, (2011, 11): 3.4,
    (2012, 3): 2.7, (2012, 6): 1.7, (2012, 9): 2.0, (2012, 11): 1.8,
    (2015, 7): 0.2, (2015, 8): 0.2, (2015, 12): 0.7,
    (2016, 2): 1.0,
    (2018, 8): 2.7, (2018, 12): 1.9,
    (2019, 5): 1.8, (2019, 6): 1.6,
    (2020, 2): 2.3, (2020, 3): 1.5, (2020, 9): 1.4,
    (2021, 2): 1.7, (2021, 3): 2.6, (2021, 11): 6.8,
    (2022, 3): 8.5, (2022, 6): 9.1, (2022, 8): 8.3, (2022, 10): 7.7, (2022, 12): 6.5,
    (2023, 7): 3.2, (2023, 10): 3.2,
    (2024, 7): 2.9, (2024, 8): 2.5, (2024, 12): 2.9,
    (2025, 4): 2.3, (2025, 10): 3.0,
    (2026, 3): 3.3,
}

# Fed funds target effective dates (midpoint of range after 2008)
FED = [
    (date(1999, 11, 16), 5.50, "5.50%"),
    (date(2000, 2, 2), 5.75, "5.75%"),
    (date(2000, 3, 21), 6.00, "6.00%"),
    (date(2000, 5, 16), 6.50, "6.50%"),
    (date(2001, 1, 3), 6.00, "6.00%"),
    (date(2001, 1, 31), 5.50, "5.50%"),
    (date(2001, 3, 20), 5.00, "5.00%"),
    (date(2001, 4, 18), 4.50, "4.50%"),
    (date(2001, 5, 15), 4.00, "4.00%"),
    (date(2001, 6, 27), 3.75, "3.75%"),
    (date(2001, 8, 21), 3.50, "3.50%"),
    (date(2001, 9, 17), 3.00, "3.00%"),
    (date(2001, 10, 2), 2.50, "2.50%"),
    (date(2001, 11, 6), 2.00, "2.00%"),
    (date(2001, 12, 11), 1.75, "1.75%"),
    (date(2002, 11, 6), 1.25, "1.25%"),
    (date(2003, 6, 25), 1.00, "1.00%"),
    (date(2004, 6, 30), 1.25, "1.25%"),
    (date(2004, 8, 10), 1.50, "1.50%"),
    (date(2004, 9, 21), 1.75, "1.75%"),
    (date(2004, 11, 10), 2.00, "2.00%"),
    (date(2004, 12, 14), 2.25, "2.25%"),
    (date(2005, 2, 2), 2.50, "2.50%"),
    (date(2005, 3, 22), 2.75, "2.75%"),
    (date(2005, 5, 3), 3.00, "3.00%"),
    (date(2005, 6, 30), 3.25, "3.25%"),
    (date(2005, 8, 9), 3.50, "3.50%"),
    (date(2005, 9, 20), 3.75, "3.75%"),
    (date(2005, 11, 1), 4.00, "4.00%"),
    (date(2005, 12, 13), 4.25, "4.25%"),
    (date(2006, 1, 31), 4.50, "4.50%"),
    (date(2006, 3, 28), 4.75, "4.75%"),
    (date(2006, 5, 10), 5.00, "5.00%"),
    (date(2006, 6, 29), 5.25, "5.25%"),
    (date(2007, 9, 18), 4.75, "4.75%"),
    (date(2007, 10, 31), 4.50, "4.50%"),
    (date(2007, 12, 11), 4.25, "4.25%"),
    (date(2008, 1, 22), 3.50, "3.50%"),
    (date(2008, 1, 30), 3.00, "3.00%"),
    (date(2008, 3, 18), 2.25, "2.25%"),
    (date(2008, 4, 30), 2.00, "2.00%"),
    (date(2008, 10, 8), 1.50, "1.50%"),
    (date(2008, 10, 29), 1.00, "1.00%"),
    (date(2008, 12, 16), 0.125, "0–0.25%"),
    (date(2015, 12, 16), 0.375, "0.25–0.50%"),
    (date(2016, 12, 14), 0.625, "0.50–0.75%"),
    (date(2017, 3, 16), 0.875, "0.75–1.00%"),
    (date(2017, 6, 15), 1.125, "1.00–1.25%"),
    (date(2017, 12, 14), 1.375, "1.25–1.50%"),
    (date(2018, 3, 22), 1.625, "1.50–1.75%"),
    (date(2018, 6, 14), 1.875, "1.75–2.00%"),
    (date(2018, 9, 27), 2.125, "2.00–2.25%"),
    (date(2018, 12, 20), 2.375, "2.25–2.50%"),
    (date(2019, 8, 1), 2.125, "2.00–2.25%"),
    (date(2019, 9, 19), 1.875, "1.75–2.00%"),
    (date(2019, 10, 31), 1.625, "1.50–1.75%"),
    (date(2020, 3, 3), 1.125, "1.00–1.25%"),
    (date(2020, 3, 16), 0.125, "0–0.25%"),
    (date(2022, 3, 17), 0.375, "0.25–0.50%"),
    (date(2022, 5, 5), 0.875, "0.75–1.00%"),
    (date(2022, 6, 16), 1.625, "1.50–1.75%"),
    (date(2022, 7, 28), 2.375, "2.25–2.50%"),
    (date(2022, 9, 22), 3.125, "3.00–3.25%"),
    (date(2022, 11, 3), 3.875, "3.75–4.00%"),
    (date(2022, 12, 15), 4.375, "4.25–4.50%"),
    (date(2023, 2, 2), 4.625, "4.50–4.75%"),
    (date(2023, 3, 23), 4.875, "4.75–5.00%"),
    (date(2023, 5, 4), 5.125, "5.00–5.25%"),
    (date(2023, 7, 27), 5.375, "5.25–5.50%"),
    (date(2024, 9, 19), 4.875, "4.75–5.00%"),
    (date(2024, 11, 8), 4.625, "4.50–4.75%"),
    (date(2024, 12, 19), 4.375, "4.25–4.50%"),
    (date(2025, 9, 18), 4.125, "4.00–4.25%"),
    (date(2025, 10, 30), 3.875, "3.75–4.00%"),
    (date(2025, 12, 11), 3.625, "3.50–3.75%"),
    (date(2026, 9, 17), 3.875, "3.75–4.00%"),
]


def fed_on(d):
    last = FED[0]
    for row in FED:
        if row[0] <= d:
            last = row
        else:
            break
    return last[2]


NARR = {
    "2000-03-10": {
        "cycle": "dotcom",
        "name": "Dot-com, first crash",
        "cause": "Greenspan hiked to 6% on 21 March. Microsoft lost the antitrust case on 3 April. The tape finally treated internet multiples as duration that could not survive 6% money. Margin calls in CSCO, YHOO and AMZN did the rest. 14 April was −9.7%, the worst day of the year.",
        "bottom": "Forced selling exhausted into the 14 April crash. The bounce the next week was oversold covering, not a Fed pivot — the 6.50% hike was still ahead.",
    },
    "2000-05-01": {
        "cycle": "dotcom",
        "name": "Last hike of the cycle",
        "cause": "16 May hike to 6.50%, the last of the tightening. The tape read it as the Fed choosing to break the bubble rather than cushion it.",
        "bottom": "Late-May oversold bounce. No policy pivot. A bear-market rally that died in the summer.",
    },
    "2000-07-17": {
        "cycle": "dotcom",
        "name": "Earnings pre-announcements",
        "cause": "Internet-cohort guidance cuts, not a macro shock. The 2000 vintage of cash-burn names started to miss.",
        "bottom": "Two-week washout, then another dead-cat bounce into the September high.",
    },
    "2000-09-01": {
        "cycle": "dotcom",
        "name": "Intel warning",
        "cause": "Intel's 21 September warning, the first in a decade. The tape stopped treating semiconductors as immune. Venture funding was already rolling over.",
        "bottom": "October oversold. Greenspan had not cut yet. Bounce was positioning, not a Fed put.",
    },
    "2000-10-20": {
        "cycle": "dotcom",
        "name": "Recount plus earnings",
        "cause": "Bush/Gore recount plus another round of tech misses. Credit started to tighten for unprofitable names.",
        "bottom": "Late-November bounce into year-end window dressing.",
    },
    "2000-12-11": {
        "cycle": "dotcom",
        "name": "Year-end de-gross",
        "cause": "Year-end de-grossing. The 2000 internet IPO vintage was being marked toward zero. NBER later dated the recession from March 2001. The tape was already there.",
        "bottom": "2 January low. The next day, 3 January, Greenspan delivered an inter-meeting 50bp cut to 6.00%. That is what started the bounce.",
    },
    "2001-01-24": {
        "cycle": "dotcom",
        "name": "Capex collapse",
        "cause": "The first 2001 bounce failed. Earnings confirmed the capex collapse at Cisco and Nortel. The Fed was cutting — 6.00% to 4.50% by 18 April — and the tape treated each cut as confirmation of how bad the economy was.",
        "bottom": "4 April, two days after a 50bp cut to 4.50%. Extreme oversold, then a sharp bear rally into May.",
    },
    "2001-05-22": {
        "cycle": "dotcom",
        "name": "September 11",
        "cause": "The May rally died on more guidance cuts. Then 11 September. Markets closed until 17 September. On the reopen the tape priced a demand shock on top of an already-broken tech cycle.",
        "bottom": "21 September, the post-9/11 washout low of this leg. The Fed had cut 50bp on 17 September to 3.00%. The airline bill and the reopening bid started the bounce.",
    },
    "2002-01-04": {
        "cycle": "dotcom",
        "name": "Enron audit premium",
        "cause": "Enron had collapsed in December. This leg was the audit premium: the tape started discounting every telecom and energy-trading name for accounting.",
        "bottom": "Late-February oversold. No policy change. Bear rally into March.",
    },
    "2002-03-08": {
        "cycle": "dotcom",
        "name": "Telecom, jobless recovery",
        "cause": "WorldCom rumors, more telecom capex collapse, the jobless-recovery narrative. The Fed on hold at 1.75%.",
        "bottom": "Early May. Another bear rally that failed.",
    },
    "2002-05-17": {
        "cycle": "dotcom",
        "name": "WorldCom",
        "cause": "WorldCom filed 21 July, then the largest bankruptcy in US history. Adelphia, Tyco. Sarbanes-Oxley in the works. The tape treated US corporate accounts as untrustworthy.",
        "bottom": "5 August oversold. SOX passed in late July. Bounce was the accounting shoe having dropped.",
    },
    "2002-08-22": {
        "cycle": "dotcom",
        "name": "Cycle low",
        "cause": "The last leg of the bear. Iraq-war premium, more restatements, a final flush of leveraged longs. Cycle low of the entire 2000–02 bear: −77.9% from 10 March 2000.",
        "bottom": "9 October 2002. Sellers ran out. The Fed cut to 1.25% on 6 November. The multi-year bull started here.",
    },
    "2002-11-27": {
        "cycle": "dotcom",
        "name": "Iraq war",
        "cause": "Iraq. The tape sold risk into the invasion. Oil up, 10-year down.",
        "bottom": "11 March, eight days before Shock and Awe on 20 March. The buy-the-war bid started as the invasion looked short.",
    },
    "2004-01-26": {
        "cycle": None,
        "name": "Measured-pace hiking",
        "cause": "The Fed's measured-pace cycle began 30 June (1.00% to 1.25%). Soft May–June payrolls, oil, and the first tightening in four years. Tech had run hard off the 2002 low.",
        "bottom": "12 August. Oil peaked in the summer scare. The tape decided a 25bp-a-meeting cycle was slow enough to live with.",
    },
    "2004-12-30": {
        "cycle": None,
        "name": "Hiking every meeting",
        "cause": "Greenspan still hiking every meeting. GM/Ford credit worries. Oil. The tape faded a mature 2003–04 rally.",
        "bottom": "Late April. Growth data held up. The Fed was still +25bp a meeting and the tape stopped fighting it.",
    },
    "2006-04-19": {
        "cycle": None,
        "name": "Last hike, inflation scare",
        "cause": "Last hikes of the cycle toward 5.25% on 29 June. CPI above 4%. The tape priced a hard landing that did not arrive in 2006.",
        "bottom": "21 July, three weeks after the final hike. Bernanke paused. Growth held. The 2006–07 melt-up started.",
    },
    "2007-10-31": {
        "cycle": "gfc",
        "name": "Bear Stearns",
        "cause": "ABX in freefall, SIVs, Countrywide. Bear Stearns itself was rescued on 16 March; the equity low of this leg was 10 March. The tape was pricing a credit event, not yet a depression.",
        "bottom": "10 March, the Bear weekend. JPMorgan/Fed backstop on 16 March. Emergency 75bp cut on 18 March to 2.25%. Relief rally into May.",
    },
    "2008-06-05": {
        "cycle": "gfc",
        "name": "Oil at $145",
        "cause": "Oil to $145. CPI 5.6%. The Fed on hold at 2% because of inflation, even as housing was collapsing. Fannie and Freddie stress.",
        "bottom": "Mid-July. Oil rolled over. Paulson/Bernanke Fannie-Freddie plan in July.",
    },
    "2008-08-14": {
        "cycle": "gfc",
        "name": "Lehman",
        "cause": "Lehman 15 September. AIG 16 September. Reserve Primary broke the buck. Commercial paper froze. This is the crash.",
        "bottom": "9–10 October, the week of the coordinated global cuts (8 October, 50bp to 1.50%) and TARP passing on 3 October after the 29 September House failure. A pause, not the cycle low.",
    },
    "2008-10-13": {
        "cycle": "gfc",
        "name": "TARP bounce fails",
        "cause": "The TARP bounce failed. More bank recapitalisation fear. European banks: Fortis, Dexia, RBS.",
        "bottom": "27 October oversold. G20, more capital injections. The Fed cut to 1.00% on 29 October.",
    },
    "2008-11-04": {
        "cycle": "gfc",
        "name": "Second crash",
        "cause": "Auto-bailout uncertainty, Citi, and the realisation that Q4 GDP would be catastrophic. The second crash.",
        "bottom": "20–21 November. Citi rescue 23 November. Obama transition. The Fed went to 0–0.25% on 16 December.",
    },
    "2009-01-06": {
        "cycle": "gfc",
        "name": "Nationalisation scare",
        "cause": "Bank nationalisation scare at Citi and Bank of America. Obama not yet inaugurated. The tape priced Sweden 1992.",
        "bottom": "20 January, Inauguration Day. The Geithner/stress-test path started to replace nationalisation.",
    },
    "2009-02-06": {
        "cycle": "gfc",
        "name": "Cycle low",
        "cause": "The last nationalisation scare. Citigroup at $1. Fiscal had passed but banks still looked insolvent. GFC cycle low: −55.6% from 31 October 2007.",
        "bottom": "9 March 2009. Citigroup had said it was profitable in January–February. The SCAP stress-test framework (10 February) finally convinced the tape recap-not-nationalise. The 2009–15 bull started here.",
    },
    "2010-04-23": {
        "cycle": None,
        "name": "Greece / flash crash",
        "cause": "Greece and EMU. Flash crash 6 May. The tape priced a European banking event and a US double-dip.",
        "bottom": "2 July. The EU/IMF Greek package and a pause in the data scare started the bounce. QE2 was still a Jackson Hole story (Bernanke, August).",
    },
    "2011-04-29": {
        "cycle": None,
        "name": "Debt ceiling, US downgrade",
        "cause": "US debt-ceiling fight. S&P downgraded the United States on 5 August. EMU second round in Italy and Spain. The tape priced a political accident in the reserve asset.",
        "bottom": "19 August, two weeks after the downgrade. Bernanke at Jackson Hole (26 August) and Operation Twist (September) were the policy put.",
    },
    "2011-09-16": {
        "cycle": None,
        "name": "Greek referendum",
        "cause": "Greek referendum scare. EMU still unresolved. Operation Twist had been announced 21 September and was not believed yet.",
        "bottom": "3 October. EU summit path, Twist starting to work through duration.",
    },
    "2011-10-27": {
        "cycle": None,
        "name": "Italian yields",
        "cause": "The EU comprehensive-summit bounce failed. Italian yields blew out. Berlusconi on the way out.",
        "bottom": "25 November. Draghi's first LTRO (8 December) was being telegraphed. Italian political change.",
    },
    "2012-03-26": {
        "cycle": None,
        "name": "Grexit round two",
        "cause": "Greek election, Spanish banks, Grexit round two. The 2012 growth scare.",
        "bottom": "1 June. Draghi's whatever-it-takes was 26 July. The June low was the growth/EMU scare exhausting before that speech.",
    },
    "2012-09-14": {
        "cycle": None,
        "name": "Fiscal cliff",
        "cause": "US fiscal cliff into the 6 November election. QE3 had been announced 13 September. The tape sold the news, then sold the cliff.",
        "bottom": "15 November, nine days after Obama's re-election. Cliff negotiations started to look solvable (settled 1 January).",
    },
    "2015-07-20": {
        "cycle": None,
        "name": "CNY devaluation",
        "cause": "PBOC devalued the yuan on 11 August. China hard-landing scare. The Fed was trying to hike (they did in December). Oil already in collapse.",
        "bottom": "25 August. PBOC/CSRC market backstop, and the Fed delayed the September hike. China-export shock, then a policy put.",
    },
    "2015-12-01": {
        "cycle": None,
        "name": "Lift-off plus oil at $26",
        "cause": "December 2015 lift-off (25bp) plus oil to $26 on 20 January plus China still leaking capital. High-yield energy stress. The tape priced a US recession that did not arrive.",
        "bottom": "11 February 2016. Draghi and Kuroda easing, oil reversal, and Yellen making clear lift-off would be slow. The Shanghai accord (27 February) later confirmed the FX put.",
    },
    "2018-08-29": {
        "cycle": None,
        "name": "Powell autopilot",
        "cause": "Powell hiking into a flattening curve. QT. The 19 December hike to 2.25–2.50% plus autopilot QT language. Section 301 tariffs on China. The tape priced a policy error.",
        "bottom": "24 December. Powell pivoted on 4 January 2019 (patient). Markets bottomed into the thin Christmas session and ran from the first trading days of January.",
    },
    "2019-05-03": {
        "cycle": None,
        "name": "China tariff tweet",
        "cause": "Trump's 5 May tweet: 25% on the remaining China goods. Huawei entity list 16 May. The tape priced a breakdown of the trade truce.",
        "bottom": "3 June. Powell on 4 June opened the door to insurance cuts. Xi-Trump G20 path. First cut 31 July.",
    },
    "2020-02-19": {
        "cycle": None,
        "name": "COVID",
        "cause": "COVID. Italy lockdown, then the US. Oil war, Saudi/Russia, 9 March. The tape priced a sudden stop of the real economy. Fastest 30% in this sample.",
        "bottom": "23 March, the day the Fed announced unlimited QE and corporate-credit facilities. Congress was days from CARES. The policy put was the bottom.",
    },
    "2020-09-02": {
        "cycle": None,
        "name": "First fade of WFH",
        "cause": "First fade of the work-from-home melt-up. CARES extras expiring. A second-wave COVID scare. Still above the 200 DMA — a bull-market correction.",
        "bottom": "23 September. Congress did not deliver a second bill then. The Fed's average-inflation targeting (Jackson Hole, 27 August) and the election-fiscal bid reasserted.",
    },
    "2021-02-12": {
        "cycle": None,
        "name": "Reflation rotation",
        "cause": "The 10-year from 1.1% to 1.6% in weeks. The tape rotated out of 2020 duration-tech into value and reopening. Still above the 200 DMA.",
        "bottom": "8 March. The 10-year stalled. Yellen and Powell did not fight the reflation. Tech found a bid as rates stopped ripping.",
    },
    "2021-11-19": {
        "cycle": "hike22",
        "name": "Retire transitory / Ukraine",
        "cause": "CPI 6.8% in November. Powell on 30 November: retire transitory. Liftoff priced for March. Russia invaded Ukraine on 24 February. The tape priced a hiking cycle into a war and commodity shock.",
        "bottom": "14 March, three days before the first 25bp hike on 16 March. A bear rally into the 29 March high, which failed.",
    },
    "2022-03-29": {
        "cycle": "hike22",
        "name": "75bp and CPI 9.1%",
        "cause": "50bp in May, then 75bp on 15 June, the day before the low. CPI 8.6% then 9.1% on 13 June. The tape priced a Volcker rerun. This is the inflation-shock leg.",
        "bottom": "16 June, the day after the 75bp hike. Positioning was max short. A summer bear rally followed.",
    },
    "2022-08-15": {
        "cycle": "hike22",
        "name": "Jackson Hole, UK LDI",
        "cause": "Powell at Jackson Hole on 26 August: pain. 75bp in September. UK LDI crisis late September. The 10-year to 4.2%. The tape priced no pivot.",
        "bottom": "12–14 October. BoE gilt intervention was 28 September. The US bottom was the 13 October CPI (7.7% vs 8.2% expected) and a peak in real yields. Near the cycle low of the 2022 bear.",
    },
    "2022-12-01": {
        "cycle": "hike22",
        "name": "Last 2022 down-leg",
        "cause": "Powell on 14 December: still restrictive, 50bp hike. Soft landing not yet believed. Tax-loss selling.",
        "bottom": "28 December. January CPI (12 January) would confirm the disinflation path. The 2023 bull started in the first week of January.",
    },
    "2023-07-19": {
        "cycle": None,
        "name": "10-year at 5%",
        "cause": "The 10-year from 3.8% to 5.0% on term premium, UST supply, QT, higher-for-longer. Israel-Hamas 7 October. Duration-tech repriced. Last hike of the cycle was 26 July to 5.25–5.50%.",
        "bottom": "26 October, a day after the Alphabet cloud miss. The 10-year failed at 5%. Payrolls and ISM then cooled in early November and the 10-year collapsed 50bp. That is the bottom.",
    },
    "2024-07-10": {
        "cycle": None,
        "name": "Yen carry unwind",
        "cause": "BoJ hiked 31 July to 0.25% and sounded hawkish. USDJPY from 161 to 142. Yen-carry unwind hit the Nikkei −12.4% on 5 August and spilled into US tech, which had been the other side of that funding. 2 August payrolls (114k) let the tape add a US-recession read. This trough printed above the 200 DMA.",
        "bottom": "7 August in the US, after the 5 August Tokyo crash. BoJ's Uchida on 7 August: no hike into instability. Carry squeeze exhausted. The Fed's September 50bp cut was then priced.",
    },
    "2024-12-16": {
        "cycle": None,
        "name": "Liberation Day tariffs",
        "cause": "Trump Liberation Day, 2 April 2025: 10% baseline plus reciprocal tariffs, China effectively 54% then 145%. China retaliated 34% then 125%. Powell warned of higher prices and weaker growth. The tape priced a global trade war and a US recession. Nasdaq closed in a bear market on 4 April.",
        "bottom": "8 April. On 9 April Trump paused reciprocal tariffs 90 days, China excluded. Nasdaq +12.2% on 9 April, the second-largest up day on record. The close of the 8th is the print low. The pause is the cause of the bottom.",
    },
    "2025-10-29": {
        "cycle": None,
        "name": "Iran / AI accountability",
        "cause": "Two things stacked. AI capex accountability — MSFT and META had been sliding from the October high as the tape started demanding returns on the spend — then the Iran/Hormuz war in March (Operation Midnight Hammer). Brent above $120. The Fed's 18 March meeting held at 3.50–3.75% and the dots showed one cut, not three. Stagflation read on duration-tech.",
        "bottom": "30 March 2026. The war premium in oil started to mean-revert and the tape decided the Fed would not re-hike. A 10% bounce off that low closed the episode. Composite later made a new high on 6 October 2026.",
    },
}

CYCLES = {
    "dotcom": {
        "label": "Dot-com bear",
        "span": "Mar 2000 – Oct 2002",
        "note": "Twelve legs inside one −77.9% bear. Peak 5,049 on 10 Mar 2000. Cycle low 1,114 on 9 Oct 2002. New high only in Apr 2015.",
        "dd": -77.9,
    },
    "gfc": {
        "label": "Global financial crisis",
        "span": "Oct 2007 – Mar 2009",
        "note": "Seven legs inside one −55.6% bear. Peak 2,859 on 31 Oct 2007. Cycle low 1,269 on 9 Mar 2009.",
        "dd": -55.6,
    },
    "hike22": {
        "label": "Hiking-cycle bear",
        "span": "Nov 2021 – Dec 2022",
        "note": "Four legs inside one −36.4% bear. Peak 16,057 on 19 Nov 2021. Cycle low 10,213 on 28 Dec 2022.",
        "dd": -36.4,
    },
}


def duration(e):
    days = e["calendar_days"]
    weeks = e["weeks"]
    months = e["months"]
    if days < 11:
        return f"{days} days"
    if months < 2:
        w = int(round(weeks))
        return f"{w} week" if w == 1 else f"{w} weeks"
    if months < 12:
        return f"{months:.1f} months ({int(round(weeks))} weeks)"
    return f"{months:.1f} months"


out = []
for e in eps:
    td = date.fromisoformat(e["trough_date"])
    pd = date.fromisoformat(e["peak_date"])
    n = NARR[e["peak_date"]]
    vs = e["vs_sma200_pct"]
    item = {
        **{k: e[k] for k in (
            "peak_date", "trough_date", "peak_month", "trough_month",
            "peak", "trough", "dd_pct", "trading_days", "calendar_days",
            "weeks", "months", "sma200", "vs_sma200_pct", "below_200dma",
            "tnx_peak", "tnx_trough", "irx_peak", "irx_trough",
        )},
        "name": n["name"],
        "cycle": n["cycle"],
        "cause": n["cause"],
        "bottom": n["bottom"],
        "duration": duration(e),
        "fed_peak": fed_on(pd),
        "fed_trough": fed_on(td),
        "cpi_peak": CPI.get((pd.year, pd.month)),
        "cpi_trough": CPI.get((td.year, td.month)),
        "dma_label": (
            f"{abs(vs):.1f}% below" if vs < 0 else f"{vs:.1f}% above"
        ),
    }
    out.append(item)

payload = {
    "asof": meta["last"]["date"],
    "last": meta["last"],
    "method": (
        "Nasdaq Composite daily closes. An episode is a peak-to-trough decline "
        "of more than 10%. It ends when the close rallies 10% off that trough, "
        "so nested legs inside a larger bear are listed separately. "
        "200 DMA is the 200-session simple average at the trough close. "
        "Rates are the Fed funds target and the 10-year yield. CPI is BLS CPI-U YoY in the trough month."
    ),
    "near_misses": [
        {
            "label": "Feb 2018 volmageddon",
            "detail": "Composite −9.7% from 26 Jan to 8 Feb. NDX did print −10.2%. Under the 10% cut on Composite, so it is not in the log.",
        },
        {
            "label": "Jun–Jul 2026",
            "detail": "Composite −9.8% from 2 Jun (27,094) to 29 Jul (24,443). NDX printed −11.3%. Under the cut on Composite.",
        },
        {
            "label": "Open now",
            "detail": (
                f"Composite closed {meta['last']['close']:,.0f} on {meta['last']['date']}, "
                f"{meta['last']['vs_ath']:.1f}% below the 6 Oct 2026 high of "
                f"{meta['last']['ath']:,.0f}. Not a qualifying episode yet. "
                f"Last close is {meta['last']['vs_sma200']:+.1f}% vs the 200 DMA."
            ),
        },
    ],
    "cycles": CYCLES,
    "episodes": out,
    "weekly": weekly,
}

open("/home/lewis/nasdaq-drawdowns/data.js", "w").write(
    "window.NDXDD = " + json.dumps(payload, separators=(",", ":")) + ";\n"
)
print("episodes", len(out), "weekly", len(weekly))
missing_narr = [e["peak_date"] for e in eps if e["peak_date"] not in NARR]
missing_cpi = [e["trough_date"] for e in out if e["cpi_trough"] is None]
print("missing narr", missing_narr)
print("missing cpi", missing_cpi)
