import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ================================
# 1. FILE PATHS
# ================================
RAW_PATH = "data/raw/Superstore Task 1 - Raw Data.csv"
PROCESSED_PATH = "data/processed/cleaned_superstore.csv"
VIS_PATH = "visuals"

# Create required folders (safe step)
os.makedirs("data/processed", exist_ok=True)
os.makedirs(VIS_PATH, exist_ok=True)

# ================================
# 2. LOAD DATA
# ================================
print("\n🔹 Loading dataset...")
df = pd.read_csv(RAW_PATH)

# ================================
# 3. CLEAN COLUMN NAMES
# ================================
print("🔹 Cleaning column names...")
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(".", "_")
)

# ================================
# 4. CLEAN DATA TYPES & MISSING VALUES
# ================================
print("🔹 Fixing data types & missing values...")

# Convert dates
if "order_date" in df.columns:
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

if "ship_date" in df.columns:
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

# Convert numbers
numeric_cols = ["sales", "profit", "quantity", "discount", "shipping_cost"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing values
if "discount" in df.columns:
    df["discount"] = df["discount"].fillna(df["discount"].median())

if "profit" in df.columns:
    df["profit"] = df["profit"].fillna(df["profit"].median())

df["state"] = df["state"].fillna("unknown")
df["country"] = df["country"].fillna("unknown")

# Remove duplicates
df.drop_duplicates(inplace=True)

# ================================
# 5. OUTLIER HANDLING (IQR)
# ================================
print("🔹 Removing outliers...")

for col in ["sales", "profit"]:
    if col in df.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        df = df[(df[col] >= lower) & (df[col] <= upper)]

# ================================
# 6. VISUALIZATIONS (MATPLOTLIB)
# ================================
print("🔹 Creating visuals...")

# ---- Sales Distribution ----
plt.figure(figsize=(8,5))
df["sales"].hist(bins=50)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{VIS_PATH}/sales_distribution.png")
plt.close()

# ---- Profit by Category ----
if "category" in df.columns:
    plt.figure(figsize=(8,5))
    df.groupby("category")["profit"].sum().plot(kind="bar")
    plt.title("Total Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig(f"{VIS_PATH}/profit_by_category.png")
    plt.close()

# ================================
# 7. SAVE CLEANED DATA
# ================================
print("🔹 Saving cleaned dataset...")
df.to_csv(PROCESSED_PATH, index=False)

print(f"\n✅ Cleaning Completed Successfully!")
print(f"📄 Cleaned file saved at: {PROCESSED_PATH}")
print(f"📊 Visuals saved in: {VIS_PATH}/\n")
