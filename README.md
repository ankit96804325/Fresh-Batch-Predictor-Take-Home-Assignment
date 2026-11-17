
# 🍟 Fresh-Batch Predictor

### A Data-Driven Fresh Food Preparation Recommendation System

**Fresh-Batch Predictor** is a Python-based decision-support tool that helps small street-food vendors determine when to prepare a fresh batch and how much food to prepare based on observed customer arrival patterns and demand.

Instead of relying entirely on guesswork, the system analyzes real-world customer traffic data collected at a food stall and provides actionable preparation recommendations.

> **Core Idea:** Prepare food at the right time, in the right quantity, to reduce food waste, minimize customer waiting time, and improve customer satisfaction.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Proposed Solution](#-proposed-solution)
- [How It Works](#-how-it-works)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Dataset and Fieldwork](#-dataset-and-fieldwork)
- [Technology Stack](#-technology-stack)
- [Installation and Setup](#-installation-and-setup)
- [How to Run](#-how-to-run)
- [Sample Output](#-sample-output)
- [Key Fieldwork Insight](#-key-fieldwork-insight)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

---

## 📖 Project Overview

Small street-food businesses often prepare food based on experience and intuition rather than recorded customer demand.

This creates two common problems:

- **Overproduction:** Food is prepared too early or in excessive quantities, resulting in wastage.
- **Underproduction:** Food is prepared too late or in insufficient quantities, causing customers to wait and potentially leave.

Fresh-Batch Predictor addresses this challenge through a simple data-driven approach.

The project uses customer arrival records collected during an evening field observation at a local samosa and pakora stall. It analyzes the collected data to estimate upcoming demand and recommend an appropriate batch size.

The goal is to make basic data analysis useful in everyday small-business operations.

---

## ❗ Problem Statement

Consider **Raju**, who runs a samosa and pakora stall outside a college's main gate.

During evening peak hours, he faces an important operational decision:

| Situation | Business Impact |
|---|---|
| Frying too early | Food becomes cold and loses freshness |
| Frying too late | Customers may wait 6–8 minutes |
| Preparing too much | Unsold food creates unnecessary waste |
| Preparing too little | Potential customers may leave |

These problems can lead to an estimated loss of ₹200–₹400 per evening through wasted food and missed sales opportunities.

Raju needs a simple system that can answer three questions:

1. When should I prepare the next batch?
2. How many customers are likely to arrive soon?
3. How many food items should I prepare?

---

## 💡 Proposed Solution

Fresh-Batch Predictor uses real-world customer arrival observations to provide practical preparation recommendations.

During one evening of fieldwork, customer arrivals, order quantities, and waiting times were manually recorded.

The collected information is stored in `data.csv`.

The Python program processes this dataset and generates recommendations based on estimated upcoming customer demand.

### Example Recommendation

At approximately 5:30 PM, the system may generate:

```text
⏰ Time: 5:30 PM

🔴 HIGH TRAFFIC EXPECTED IN NEXT 10 MINUTES!

📊 Expected Customers: ~12
🍟 Expected Items: ~26

👉 RECOMMENDATION:
   Prepare a fresh batch of 32 items NOW.

⏳ Estimated Frying Time: 7 minutes

💡 The batch should be ready around
   the expected increase in customer demand.
```

*Note: This is an illustrative example, not a verified prediction result.*

---

## ⚙️ How It Works

The project follows a straightforward data-processing workflow.

```text
Customer Arrival Observations
            |
            v
       data.csv
            |
            v
     Data Processing
            |
            v
   Traffic and Demand Analysis
            |
            v
  Upcoming Demand Estimation
            |
            v
    Traffic Classification
            |
            v
   Fresh-Batch Recommendation
            |
            v
   Vendor Preparation Decision
```

### Step-by-Step Workflow

1. **Data Collection:** Customer arrival events are manually recorded at the food stall.
2. **Data Loading:** The Python script reads the collected records from `data.csv`.
3. **Data Analysis:** The program analyzes customer traffic and order information.
4. **Demand Estimation:** The system estimates upcoming customer and food-item demand.
5. **Traffic Classification:** Predicted traffic is classified into LOW, MEDIUM, or HIGH.
6. **Batch Recommendation:** The system recommends when to prepare a fresh batch and how many items to prepare.

---

## ✨ Key Features

- **Customer Traffic Analysis:** Understands traffic patterns using recorded customer arrival information.
- **Demand Estimation:** Estimates upcoming customer and food-item demand.
- **Traffic Classification:** Identifies expected traffic intensity.
- **Batch Size Recommendation:** Suggests an appropriate preparation quantity.
- **Frying-Time Consideration:** Accounts for the approximate 7-minute preparation time.
- **Interactive Execution:** Allows users to query recommendations for a specific time.
- **Traffic Report:** Provides an overview of collected traffic data.

---

## 📁 Project Structure

```text
Fresh-Batch-Predictor-Take-Home-Assignment/
│
├── data.csv
├── predictor.py
├── research.md
├── reflection.md
├── ai-chats/
├── README.md
└── .gitignore
```

| File / Folder | Description |
|---|---|
| `data.csv` | Customer arrival and order records collected during fieldwork |
| `predictor.py` | Main Python program for traffic analysis and batch recommendations |
| `research.md` | Problem research, user identification, and fieldwork planning |
| `reflection.md` | Project reflection, observations, learnings, and limitations |
| `ai-chats/` | AI conversation records used during development |
| `README.md` | Project documentation |
| `.gitignore` | Files Git should ignore |

---

## 📊 Dataset and Fieldwork

An important part of this project was collecting actual customer behavior observations rather than relying entirely on artificially generated data.

### Fieldwork Details

| Parameter | Details |
|---|---|
| Observation Date | 17 November 2026 |
| Location | Raju Snacks Corner, outside main gate, [College Name] |
| Observation Time | 4:30 PM – 7:00 PM |
| Data Collection Method | Manual observation |
| Total Recorded Entries | 23 |
| Data Storage | CSV file |

### Information Collected

- Customer arrival time
- Number of customers arriving
- Food items ordered
- Customer waiting time

### Data Collection Methodology

- Time was recorded using a phone clock.
- Customer headcount was estimated visually.
- Orders were recorded by observing and listening to customer interactions.
- Waiting time was measured using a stopwatch.

The collected observations were organized into `data.csv` for analysis.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| Pandas | Dataset loading and data analysis |
| Matplotlib | Optional data visualization |
| CSV | Customer observation data storage |
| Git & GitHub | Version control and project hosting |
| VS Code | Development environment |

---

## 🚀 Installation and Setup

### Prerequisites

Make sure you have installed:

- Python 3.8 or above
- pip (Python package manager)
- Git
- Visual Studio Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/ankit96804325/Fresh-Batch-Predictor-Take-Home-Assignment.git
```

### 2. Navigate to the Project Directory

```bash
cd Fresh-Batch-Predictor-Take-Home-Assignment
```

### 3. Install Dependencies

```bash
pip install pandas matplotlib
```

Matplotlib is optional if you are not using visualization functionality.

---

## ▶️ How to Run

### 1. Interactive Mode

Run the predictor:

```bash
python predictor.py
```

This starts the interactive interface, allowing you to enter a time and receive a recommendation.

### 2. Direct Time Query

To check expected traffic for a particular time:

```bash
python predictor.py "5:30 PM"
```

### 3. Full Traffic Report

To generate the traffic report:

```bash
python predictor.py --report
```

**Note:** These commands reflect the intended interface. Adjust them if the actual argument handling in `predictor.py` differs.

---

## 📟 Sample Output

An illustrative example of a recommendation:

```text
========================================
       FRESH-BATCH PREDICTOR 🍟
========================================

Time: 5:30 PM

Traffic Forecast:
----------------------------------------
Expected Traffic  : HIGH
Expected Customers: 12
Expected Items    : 26

Batch Recommendation:
----------------------------------------
Action            : DROP A FRESH BATCH
Recommended Batch : 32 Items
Frying Time       : 7 Minutes

----------------------------------------
Recommendation:
Prepare the next batch now to meet
the expected increase in demand.
========================================
```

---

## 🚌 Key Fieldwork Insight

### Raju doesn't need to watch the clock — he needs to watch the bus!

One of the most interesting discoveries during fieldwork was the relationship between public transport and customer traffic.

The 5:45 PM city bus from the industrial area drops factory workers near the stall, creating another wave of customers.

This observation suggests that customer demand is influenced not only by time but also by real-world events.

This insight came from speaking with Raju and observing the stall, rather than simply analyzing the CSV dataset.

It also reveals an opportunity to improve the predictor by incorporating external demand signals such as bus arrival times.

---

## ⚠️ Limitations

Although the project demonstrates a practical application of data analysis, there are some limitations:

1. **Limited Dataset:** The system is based on only one evening of observations (23 recorded entries).
2. **Day-to-Day Variation:** Customer traffic may differ across weekdays, weekends, and special occasions.
3. **Weather Conditions:** Rain and temperature may influence customer arrivals.
4. **College Schedule:** Holidays, examinations, and college events may change demand.
5. **External Events:** Bus arrivals and nearby activities can create sudden traffic spikes.
6. **Manual Thresholds:** Traffic classification thresholds are manually defined and may need adjustment.
7. **Prediction Accuracy:** Recommendations are estimates based on limited historical observations, not guaranteed outcomes.

The current version should be treated as a decision-support tool, not a fully automated forecasting system.

---

## 🔮 Future Improvements

There are several opportunities to extend this project:

- **More Data Collection:** Collect customer arrival data across multiple days and weeks.
- **Machine Learning Integration:** Explore regression or time-series forecasting models when sufficient historical data becomes available.
- **Weather Integration:** Consider weather conditions while estimating demand.
- **Bus Arrival Detection:** Include known transport schedules as an additional demand signal.
- **Interactive Dashboard:** Develop a dashboard for vendors to view traffic patterns.
- **Dynamic Batch Sizing:** Improve batch-size recommendations using historical demand and inventory information.
- **Real-Time Data Collection:** Create a mobile interface for recording customer arrivals.
- **Performance Evaluation:** Compare predicted demand with actual customer arrivals using suitable error metrics.

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Identifying real-world problems through field observation.
- Understanding the needs of a small-business user.
- Collecting and organizing real-world data.
- Working with CSV datasets using Python and Pandas.
- Analyzing customer arrival and demand patterns.
- Translating data insights into actionable recommendations.
- Understanding the importance of data quality and sample size.
- Recognizing the limitations of simple forecasting approaches.
- Using Git and GitHub for project version control and documentation.

The biggest takeaway was that even a small amount of carefully collected real-world data can help identify useful patterns and support better everyday decisions.

---

## 👨‍💻 Author

**Ankit **

B.Tech Student  
[ECE'27]  
[NIT JSR]

**Project:** Fresh-Batch Predictor  
**Date:** 17 November 2026

### GitHub Repository

[Fresh-Batch-Predictor-Take-Home-Assignment](https://github.com/ankit96804325/Fresh-Batch-Predictor-Take-Home-Assignment)

---

## ⭐ Acknowledgment

This project was developed as a practical exploration of how simple data analysis can solve everyday operational challenges faced by small street-food vendors.

**Built with Python, real-world observations, and a focus on practical problem-solving.** 🍟
