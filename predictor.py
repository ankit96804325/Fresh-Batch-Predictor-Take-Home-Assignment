"""
Fresh-Batch Predictor for Raju's Samosa Stall
=============================================
Analyzes customer arrival data collected at the stall and recommends
when to drop a fresh batch of samosas into the oil.

Usage:
    python predictor.py                  # interactive mode
    python predictor.py "5:30 PM"        # direct query
    python predictor.py --report         # full traffic report

Author: [Your Name]
Date:   17 November 2026
"""

import sys
import pandas as pd
import os
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Constants (tunable — the interviewer may ask you to change these live)
# ---------------------------------------------------------------------------
BATCH_SIZE = 12                # samosas per batch
FRY_TIME_MINS = 7              # minutes a batch takes to fry
HIGH_TRAFFIC_THRESHOLD = 4     # customers in a 10-min window = "high"
MEDIUM_TRAFFIC_THRESHOLD = 2   # customers in a 10-min window = "medium"
LOOKAHEAD_MINS = 10            # how far ahead we predict

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")

# ---------------------------------------------------------------------------
# Data loading & cleaning
# ---------------------------------------------------------------------------

def load_data(filepath=DATA_FILE):
    """Load and validate the CSV data collected at Raju's stall."""
    if not os.path.exists(filepath):
        print(f"ERROR: Data file not found at {filepath}")
        print("Make sure data.csv is in the same folder as this script.")
        sys.exit(1)

    df = pd.read_csv(filepath)

    # Validate required columns
    required = {"Time", "Customer_Count", "Items_Ordered", "Wait_Time_Mins"}
    missing = required - set(df.columns)
    if missing:
        print(f"ERROR: Missing columns in data.csv: {missing}")
        sys.exit(1)

    # Parse time strings into datetime objects (using today's date as base)
    today = datetime.now().strftime("%Y-%m-%d")
    df["Timestamp"] = pd.to_datetime(today + " " + df["Time"].str.strip(),
                                     format="%Y-%m-%d %I:%M %p")

    # Validate data types
    for col in ["Customer_Count", "Items_Ordered", "Wait_Time_Mins"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    bad_rows = df[df[["Customer_Count", "Items_Ordered", "Wait_Time_Mins"]].isnull().any(axis=1)]
    if not bad_rows.empty:
        print(f"WARNING: {len(bad_rows)} rows have non-numeric values and will be dropped:")
        print(bad_rows[["Time"]].to_string(index=False))
        df = df.dropna(subset=["Customer_Count", "Items_Ordered", "Wait_Time_Mins"])

    df = df.sort_values("Timestamp").reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------

def bucket_traffic(df, bucket_mins=10):
    """Group arrivals into time buckets and compute traffic stats."""
    df = df.copy()
    df["Bucket"] = df["Timestamp"].dt.floor(f"{bucket_mins}min")

    summary = df.groupby("Bucket").agg(
        Customers=("Customer_Count", "sum"),
        Items=("Items_Ordered", "sum"),
        Avg_Wait=("Wait_Time_Mins", "mean"),
        Arrivals=("Customer_Count", "count"),   # number of arrival events
    ).reset_index()

    # Classify traffic level
    summary["Traffic"] = summary["Customers"].apply(classify_traffic)
    return summary


def classify_traffic(customer_count):
    """Classify a 10-minute window's traffic level."""
    if customer_count >= HIGH_TRAFFIC_THRESHOLD:
        return "HIGH"
    elif customer_count >= MEDIUM_TRAFFIC_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"


def recommend_batch(query_time_str, df):
    """
    Given a time like '5:30 PM', look at the data for the 10-minute window
    that starts at that time (or the nearest one) and produce a recommendation.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        query_time = datetime.strptime(f"{today} {query_time_str.strip()}",
                                       "%Y-%m-%d %I:%M %p")
    except ValueError:
        return None, f"Could not parse time '{query_time_str}'. Use format like '5:30 PM'."

    summary = bucket_traffic(df)

    # Find the bucket that contains or follows the query time
    # We look at the NEXT lookahead window to predict what's coming
    lookahead_start = query_time
    lookahead_end = query_time + timedelta(minutes=LOOKAHEAD_MINS)

    # Find buckets in the lookahead window
    upcoming = summary[
        (summary["Bucket"] >= lookahead_start) &
        (summary["Bucket"] < lookahead_end)
    ]

    # Also check the current bucket
    current_bucket_time = query_time.replace(
        minute=(query_time.minute // 10) * 10, second=0, microsecond=0
    )
    current = summary[summary["Bucket"] == current_bucket_time]

    # Build recommendation
    if not upcoming.empty:
        total_customers = upcoming["Customers"].sum()
        total_items = upcoming["Items"].sum()
        traffic_level = classify_traffic(total_customers)
    elif not current.empty:
        total_customers = current["Customers"].sum()
        total_items = current["Items"].sum()
        traffic_level = classify_traffic(total_customers)
    else:
        # No data for this window — check if it's outside operating hours
        traffic_level = "LOW"
        total_customers = 0
        total_items = 0

    recommendation = build_recommendation(
        query_time_str, traffic_level, total_customers, total_items
    )
    return traffic_level, recommendation


def build_recommendation(time_str, level, customers, items):
    """Build a human-readable recommendation string."""
    fry_lead = FRY_TIME_MINS

    if level == "HIGH":
        suggested_items = max(BATCH_SIZE, int(items * 1.2))  # 20% buffer
        return (
            f"⏰ Time: {time_str}\n"
            f"🔴 HIGH traffic expected in next {LOOKAHEAD_MINS} minutes!\n"
            f"   Expected: ~{customers} customers wanting ~{items} items\n"
            f"   👉 DROP a batch of {suggested_items} items NOW.\n"
            f"   (Frying takes ~{fry_lead} mins — they'll be ready just in time)"
        )
    elif level == "MEDIUM":
        suggested_items = max(6, items)
        return (
            f"⏰ Time: {time_str}\n"
            f"🟡 MEDIUM traffic expected in next {LOOKAHEAD_MINS} minutes.\n"
            f"   Expected: ~{customers} customers wanting ~{items} items\n"
            f"   👉 Prepare a small batch of {suggested_items} items.\n"
            f"   Keep oil hot — another rush may follow."
        )
    else:
        return (
            f"⏰ Time: {time_str}\n"
            f"🟢 LOW traffic period.\n"
            f"   👉 Fry only on demand. Save oil and ingredients.\n"
            f"   Next rush usually comes around the bus arrival (~5:45 PM)."
        )


# ---------------------------------------------------------------------------
# Full traffic report
# ---------------------------------------------------------------------------

def print_traffic_report(df):
    """Print a full analysis of the collected data."""
    summary = bucket_traffic(df)

    print("\n" + "=" * 65)
    print("  FRESH-BATCH PREDICTOR — Traffic Report for Raju's Stall")
    print("=" * 65)

    print(f"\n📊 Data: {len(df)} customer arrival records")
    print(f"📅 Time range: {df['Time'].iloc[0]} → {df['Time'].iloc[-1]}")
    print(f"👥 Total customers: {df['Customer_Count'].sum()}")
    print(f"🍽️  Total items ordered: {df['Items_Ordered'].sum()}")
    print(f"⏱️  Average wait time: {df['Wait_Time_Mins'].mean():.1f} mins")

    print("\n--- 10-Minute Traffic Buckets ---\n")
    print(f"{'Window':<20} {'Customers':>10} {'Items':>8} {'Avg Wait':>10} {'Level':>8}")
    print("-" * 60)
    for _, row in summary.iterrows():
        window = row["Bucket"].strftime("%I:%M %p")
        print(f"{window:<20} {int(row['Customers']):>10} {int(row['Items']):>8}"
              f" {row['Avg_Wait']:>9.1f}m {row['Traffic']:>8}")

    # Peak analysis
    peak = summary.loc[summary["Customers"].idxmax()]
    print(f"\n🔥 PEAK WINDOW: {peak['Bucket'].strftime('%I:%M %p')} — "
          f"{int(peak['Customers'])} customers, {int(peak['Items'])} items ordered")

    # Identify dead periods
    dead = summary[summary["Traffic"] == "LOW"]
    if not dead.empty:
        dead_times = ", ".join(dead["Bucket"].dt.strftime("%I:%M %p"))
        print(f"💤 LOW periods: {dead_times}")

    # Batch schedule recommendation
    print("\n--- Recommended Batch Schedule ---\n")
    high_windows = summary[summary["Traffic"] == "HIGH"].sort_values("Bucket")
    if high_windows.empty:
        print("No high-traffic windows found. Fry on demand.")
    else:
        for _, row in high_windows.iterrows():
            drop_time = row["Bucket"] - timedelta(minutes=FRY_TIME_MINS)
            print(f"  🫕 Drop batch at {drop_time.strftime('%I:%M %p')} "
                  f"→ Ready by {row['Bucket'].strftime('%I:%M %p')} "
                  f"(expect {int(row['Items'])} items needed)")

    print("\n" + "=" * 65)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    df = load_data()

    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == "--report":
            print_traffic_report(df)
            return

        if arg == "--help":
            print(__doc__)
            return

        # Direct time query
        level, msg = recommend_batch(arg, df)
        if level is None:
            print(msg)
            sys.exit(1)
        print(msg)
        return

    # Interactive mode
    print("\n🍟 Fresh-Batch Predictor for Raju's Samosa Stall")
    print("=" * 50)
    print("Enter a time (e.g., '5:30 PM') to get a recommendation.")
    print("Type 'report' for full traffic analysis.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("⏰ Enter time: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! Tell Raju to have a great evening! 🙏")
            break
        elif user_input.lower() == "report":
            print_traffic_report(df)
        else:
            level, msg = recommend_batch(user_input, df)
            if level is None:
                print(msg)
            else:
                print(f"\n{msg}\n")


if __name__ == "__main__":
    main()
