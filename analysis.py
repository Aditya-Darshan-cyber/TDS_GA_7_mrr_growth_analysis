import pandas as pd
import matplotlib.pyplot as plt

# --- Load data ---
df = pd.read_csv("data/mrr_2024.csv")  # Quarter, MRR_Growth

# --- Constants ---
INDUSTRY_TARGET = 15.0

# --- Calculations ---
average = df["MRR_Growth"].mean()
# Print exactly 7.34 when using this data
print("Average MRR Growth:", f"{average:.2f}")

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", label="Company MRR Growth")
plt.axhline(y=INDUSTRY_TARGET, linestyle="--", label="Industry Target (15)")
plt.title("Quarterly MRR Growth vs Industry Target (2024)")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.grid(True)
plt.legend()

# --- Save chart ---
plt.tight_layout()
plt.savefig("mrr_growth.png", dpi=300)
# (If you run locally, you can also show it:)
# plt.show()
