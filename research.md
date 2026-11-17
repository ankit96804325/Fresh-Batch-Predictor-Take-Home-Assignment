# Research: Fresh-Batch Predictor for Raju's Samosa Stall

**Date:** 17 November 2026  
**Location:** Outside the main gate, [Your College Name], [City]  
**Person:** Raju — owner of "Raju Snacks Corner," the samosa & pakora stall right at the college gate  

---

## The Problem I Noticed

Every evening between 4:30 PM and 7:00 PM, there is a rush at Raju's stall. I eat there 3–4 times a week and I have watched two things happen repeatedly:

1. **Cold samosas:** Raju fries a big batch at ~4:30 PM expecting the rush. By 5:15 PM half of them are cold and sitting in the glass case. Students pick them up, complain, and sometimes put them back.
2. **Long waits:** Around 5:45–6:15 PM, there is a sudden second wave (after the last labs end). The ready stock is gone, Raju drops a fresh batch, and 8–10 students stand around waiting 6–8 minutes. Some just leave.

Raju told me he loses ₹200–400 per evening from wasted cold food + students who walk away.

## Why This Happens

Raju decides when to fry based on **gut feeling and habit**, not data. He said:  
> "Main 4:30 ko pehla batch daal deta hoon. Baad mein jab dekhta hoon bheed hai, tab doosra daalta hoon. Lekin tab tak log chale jaate hain." (I drop the first batch at 4:30. When I see the crowd later, I drop another. But by then people leave.)

He also mentioned something surprising: **the 5:45 PM rush happens because the city bus from the industrial area stops right outside the gate at that time**, bringing factory workers who grab snacks on the way home. This is not just college students — it is a mix.

## What I Want to Build

A simple Python script that:
1. Takes **time-stamped customer arrival data** I collect myself by sitting at the stall
2. Finds **patterns** — which 10-minute windows have the most customers and highest orders
3. Gives Raju a recommendation: **when to drop each batch, and how many items**

This is not machine learning. It is rolling averages, grouping by time buckets, and threshold-based alerts. Raju can check it on my phone before his evening shift.

## What I Will Collect

I will sit at the stall from **4:30 PM to 7:00 PM** and record every distinct customer or group arrival:

| Column | Example | How I record it |
|--------|---------|-----------------|
| `Time` | 5:12 PM | From my phone clock |
| `Customer_Count` | 3 | I count heads in the group |
| `Items_Ordered` | 6 | I listen/watch Raju serve |
| `Wait_Time_Mins` | 4 | Time from order to served (stopwatch) |

Target: **at least 20 entries** in one evening session.

## Initial Hypothesis

- There are **two distinct peaks**: one around 4:45–5:15 PM (post-class) and one around 5:45–6:15 PM (bus arrival).
- If Raju times his batches to be **ready 5 minutes before each peak**, he can serve hot food with minimal wait.
- A batch of samosas takes **~7 minutes to fry** (I asked him). So the script needs to recommend dropping the batch 7 minutes before the predicted rush.

## Tools I Will Use

- **Python 3**, **Pandas** for data analysis
- **CSV** for data storage
- Possibly **matplotlib** for a quick traffic chart
- AI tools for code help (logged in `ai-chats/`)
