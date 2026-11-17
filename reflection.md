# Reflection

## What I Expected vs. What Actually Happened

### Going In
I assumed Raju's problem was simple: he makes too many samosas too early. I expected the data would show one clean bell-curve of demand around 5 PM, and the fix would be "just fry later."

### What I Found
The data showed **two distinct peaks**, not one. The first peak (around 5:00–5:15 PM) is college students leaving class. The second peak (around 5:45–6:00 PM) is **factory workers getting off the city bus** that stops right outside the gate. I did not know about this bus pattern until Raju told me. This was the most surprising part of the fieldwork.

Raju said something that stuck with me: *"Mujhe ghadi nahi dekhni chahiye, mujhe bus dekhni chahiye."* (I shouldn't watch the clock, I should watch the bus.) This completely reframed the problem. The trigger for the second batch isn't a time — it's an event.

## What the Tool Can and Cannot Do

### What it does well:
- It correctly identifies the two rush windows from the data
- The batch timing recommendations account for the 7-minute frying time
- It gives clear, actionable advice in simple language Raju could follow

### What it should NOT be trusted for:
- **Rainy days or holidays**: The data is from one normal weekday evening. On a rainy day or during exams, the pattern would be completely different. Raju should not blindly follow the tool on unusual days.
- **Weekend patterns**: I only collected data on a weekday. Weekend foot traffic might be different — fewer students, more families.
- **Menu changes**: If Raju adds new items (say, bread pakora), the items-per-customer ratio would change.
- **The bus variable**: If the city bus schedule changes, the second peak shifts. The tool uses historical time-based data, so it wouldn't catch this automatically.

## What I Would Improve With More Time

1. **Multiple days of data**: One evening gives a snapshot, but 5–7 days would show variance and make predictions more reliable.
2. **A "bus arrival" column**: Since the bus is a key trigger, tracking whether a bus just arrived (yes/no) would make the model smarter.
3. **Weather flag**: Adding a weather column to see how rain affects footfall.
4. **A simple phone alert**: Instead of Raju running a script, a WhatsApp bot or SMS at key times ("Drop batch now!") would be more practical for him.

## What I Learned About Building for Real People

Building a tool that works technically is easy. Building one that helps a real person requires **sitting with them and understanding their world**. The most important thing I learned was not from the code — it was that Raju's decision trigger is the bus, not the clock. No amount of coding from my room would have revealed that.

Also, Raju was skeptical at first ("Yeh sab phone mein kya hoga?") but when I showed him the traffic chart and said "Drop 15 samosas at 5:38 PM," he nodded and said "Haan, yeh sahi lag raha hai." That felt like the real validation — not the code running, but the nod.
