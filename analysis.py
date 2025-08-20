# analysis.py
# Author: 24f2003053@ds.study.iitm.ac.in
# Updated analysis file for PR checks
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -----------------------------
# Data: 2024 Quarterly Scores
# -----------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Score":   [3.36, 6.22, 3.28, 6.81],  # given
}
target = 4.5  # Industry benchmark

df = pd.DataFrame(data)
avg = df["Score"].mean()

# Assert average is 4.92 (as required, allow small rounding tolerance)
if not math.isclose(round(avg, 2), 4.92, abs_tol=0.01):
    raise ValueError(f"Average must be 4.92; computed {avg:.2f}")

print(f"Average satisfaction score (2024): {avg:.2f}")
print(f"Target: {target:.2f}. Delta to target: {avg - target:+.2f}")

# -----------------------------
# Styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

fig_dir = Path("figures")
fig_dir.mkdir(exist_ok=True)

# -----------------------------
# Plot 1: Trend vs Benchmark
# -----------------------------
plt.figure(figsize=(10, 6))
ax = sns.lineplot(data=df, x="Quarter", y="Score", marker="o", linewidth=3)
ax.axhline(target, linestyle="--", linewidth=2, label=f"Industry Target = {target}", color="tab:red")

# Annotate points
for x, y in zip(df["Quarter"], df["Score"]):
    ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center")

# Title/Subtitles
ax.set_title("Patient Satisfaction Trend (2024) vs. Industry Benchmark", fontweight="bold", pad=14)
ax.set_ylabel("Satisfaction Score")
ax.set_xlabel("Quarter")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig(fig_dir / "trend_vs_benchmark.png", dpi=150)
plt.close()

# -----------------------------
# Plot 2: Bars vs Benchmark
# -----------------------------
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df, x="Quarter", y="Score")
ax.axhline(target, linestyle="--", linewidth=2, color="tab:red", label=f"Target = {target}")

# Labels
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f"{height:.2f}", (p.get_x() + p.get_width()/2.0, height),
                ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')

ax.set_title("Quarterly Scores vs. Target", fontweight="bold", pad=14)
ax.set_ylabel("Satisfaction Score")
ax.set_xlabel("Quarter")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig(fig_dir / "bars_vs_benchmark.png", dpi=150)
plt.close()

# -----------------------------
# Simple console summary
# -----------------------------
below = df[df["Score"] < target]["Quarter"].tolist()
above = df[df["Score"] >= target]["Quarter"].tolist()
print(f"Quarters below target ({target}): {below}")
print(f"Quarters at/above target: {above}")

print("Analysis complete. Figures saved in ./figures/")
