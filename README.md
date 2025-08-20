# Healthcare Performance Analysis (2024) — Patient Satisfaction

**Analyst:** 24f2003053@ds.study.iitm.ac.in

This pull request provides code and visuals to analyze 2024 quarterly patient satisfaction scores versus the industry benchmark, and a concise, actionable data story for executives.

## Dataset
- **Quarterly Scores (2024):**  
  - Q1: 3.36  
  - Q2: 6.22  
  - Q3: 3.28  
  - Q4: 6.81  
- **Average (required):** **4.92**  
- **Industry Target:** **4.50**

> The Python script validates the average as 4.92.

## Key Findings
1. **Volatility:** Scores swing significantly quarter-to-quarter (3.28–6.81), indicating inconsistent patient experience across the year.
2. **Target comparison:** With an annual **average of 4.92**, we are **+0.42 above** the target of 4.5 overall; however, **Q1 (3.36)** and **Q3 (3.28)** underperform and risk reputational damage if that pattern persists.
3. **Seasonality / Operational strain:** Underperformance in Q1 and Q3 suggests potential seasonal staffing or operational bottlenecks (e.g., post-holiday backlog, resource rotation, capacity mismatches).

## Business Implications
- **Inconsistent experience** erodes trust and NPS despite a safe annual average.
- **Resource allocation** should account for forecasted demand spikes in Q1/Q3 to avoid recurring dips.
- **Executive oversight:** Volatility elevates risk for payer contracts and accreditation if low quarters coincide with audits.

## Recommendations (to reach/maintain ≥ 4.5 sustainably)
**Core solution:** *Improve service quality and wait times.*

1. **Wait-time compression**
   - Introduce **real-time queue dashboards** and SLA alerts for triage and front-desk.
   - **Flex staffing** model in Q1/Q3; cross-train float pool for peak hours.
   - Pilot **fast-track lanes** for low-acuity cases to reduce bottlenecks.

2. **Quality of interaction**
   - Standardize **empathy scripting**; run monthly **micro-coaching** on communication.
   - Add **post-visit SMS check-ins** with short CSAT to catch issues early.

3. **Process & Ops**
   - **Root-cause analysis** of Q1/Q3 (provider coverage, rooms, diagnostics turnaround).
   - **Capacity planning** using historic arrivals; optimize scheduling templates.
   - Improve **handoffs** (front desk → nurse → physician → discharge).

4. **Measurement & accountability**
   - Weekly CSAT review with a **variance-to-target dashboard**.
   - Tie unit-level bonuses to **wait-time SLA** and **CSAT delta vs. last quarter**.

## How to Reproduce
```bash
# create environment (optional)
python -m venv .venv && source .venv/bin/activate

pip install pandas matplotlib seaborn

python analysis.py
# figures saved to ./figures/
