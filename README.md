# Fresh-Batch Predictor 🍟

**A simple tool that tells a street-food vendor when to drop a fresh batch into the oil — based on real customer traffic data collected at the stall.**

---

## The Problem

**Raju** runs a samosa & pakora stall outside [College Name]'s main gate. Every evening he faces a dilemma:
- Fry too early → food gets cold, customers complain
- Fry too late → customers wait 6–8 minutes and walk away
- He loses ₹200–400 per evening from wasted food and lost customers

## The Solution

I sat at Raju's stall for one evening (4:30 PM – 7:00 PM) during peak hours and recorded every customer arrival: how many people came, what they ordered, and how long they waited. This data lives in `data.csv` (23 entries).

The `predictor.py` script analyzes this data and gives Raju a simple recommendation:

```
⏰ Time: 5:30 PM
🔴 HIGH traffic expected in next 10 minutes!
   Expected: ~12 customers wanting ~26 items
   👉 DROP a batch of 32 items NOW.
   (Frying takes ~7 mins — they'll be ready just in time)
```

## How to Run

### Requirements
```
Python 3.8+
pandas
matplotlib (optional, for charts)
```

### Install
```bash
pip install pandas matplotlib
```

### Usage

**Interactive mode:**
```bash
python predictor.py
```

**Direct query:**
```bash
python predictor.py "5:30 PM"
```

**Full traffic report:**
```bash
python predictor.py --report
```

## Files

| File | Description |
|------|-------------|
| `research.md` | Problem identification, person details, fieldwork plan |
| `data.csv` | 23 real customer arrival records collected at the stall |
| `predictor.py` | Main Python script — the Fresh-Batch Predictor |
| `reflection.md` | What I learned, what surprised me, tool limitations |
| `ai-chats/` | Exported AI conversations used during development |

## Key Fieldwork Finding

Raju doesn't need to watch the **clock** — he needs to watch the **bus**. The 5:45 PM city bus from the industrial area drops factory workers right at the gate, causing the second rush. This insight came from talking to Raju, not from the data.

## Data Collection Details

- **Date:** 17 November 2026
- **Location:** Raju Snacks Corner, outside main gate, [College Name]
- **Time window:** 4:30 PM – 7:00 PM
- **Method:** Manual recording on phone (time from clock, headcount by eye, orders by watching/listening, wait time by stopwatch)
- **Entries:** 23 arrival events

## Limitations

- Based on **one evening** of data — patterns may vary by day
- Does not account for **weather, holidays, or exam schedules**
- The bus-arrival trigger is noted but not yet coded as a feature
- Thresholds are manually set and would benefit from more data

## Author

[Your Name]  
B.Tech [Your Branch], [College Name]  
17 November 2026
