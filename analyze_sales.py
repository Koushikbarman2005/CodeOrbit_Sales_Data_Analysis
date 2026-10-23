"""
Sales Data Analysis with Pandas
================================
Input : sales_data.csv
Output: analysis_log.txt (key metrics + summaries, printed and logged)
        Also produces CSVs for each summary table for use in the report/Excel.
"""
import pandas as pd

log_lines = []
def log(msg):
    print(msg)
    log_lines.append(str(msg))

df = pd.read_csv("sales_data.csv", parse_dates=["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
df["Quarter"] = df["OrderDate"].dt.to_period("Q").astype(str)

log(f"Loaded {len(df)} orders spanning {df['OrderDate'].min().date()} to {df['OrderDate'].max().date()}\n")

# -----------------------------------------------------------------
# Key metrics
# -----------------------------------------------------------------
total_sales = df["Sales"].sum()
total_orders = df["OrderID"].nunique()
avg_order_value = df["Sales"].mean()
total_units = df["Quantity"].sum()

log("=== KEY METRICS ===")
log(f"Total Sales: ${total_sales:,.2f}")
log(f"Total Orders: {total_orders}")
log(f"Average Order Value: ${avg_order_value:,.2f}")
log(f"Total Units Sold: {total_units}\n")

# -----------------------------------------------------------------
# Top products
# -----------------------------------------------------------------
top_products = (
    df.groupby("Product")
      .agg(Total_Sales=("Sales", "sum"), Units_Sold=("Quantity", "sum"), Orders=("OrderID", "nunique"))
      .sort_values("Total_Sales", ascending=False)
      .reset_index()
)
top_products.to_csv("top_products.csv", index=False)
log("=== TOP 5 PRODUCTS BY SALES ===")
log(top_products.head(5).to_string(index=False) + "\n")

# -----------------------------------------------------------------
# Sales by category
# -----------------------------------------------------------------
by_category = (
    df.groupby("Category")
      .agg(Total_Sales=("Sales", "sum"), Units_Sold=("Quantity", "sum"), Orders=("OrderID", "nunique"))
      .sort_values("Total_Sales", ascending=False)
      .reset_index()
)
by_category["Pct_of_Total"] = (by_category["Total_Sales"] / total_sales * 100).round(1)
by_category.to_csv("sales_by_category.csv", index=False)
log("=== SALES BY CATEGORY ===")
log(by_category.to_string(index=False) + "\n")

# -----------------------------------------------------------------
# Sales by region
# -----------------------------------------------------------------
by_region = (
    df.groupby("Region")
      .agg(Total_Sales=("Sales", "sum"), Units_Sold=("Quantity", "sum"), Orders=("OrderID", "nunique"))
      .sort_values("Total_Sales", ascending=False)
      .reset_index()
)
by_region["Pct_of_Total"] = (by_region["Total_Sales"] / total_sales * 100).round(1)
by_region.to_csv("sales_by_region.csv", index=False)
log("=== SALES BY REGION ===")
log(by_region.to_string(index=False) + "\n")

# -----------------------------------------------------------------
# Sales by month (time period trend)
# -----------------------------------------------------------------
by_month = (
    df.groupby("Month")
      .agg(Total_Sales=("Sales", "sum"), Orders=("OrderID", "nunique"))
      .reset_index()
      .sort_values("Month")
)
by_month.to_csv("sales_by_month.csv", index=False)
log("=== SALES BY MONTH ===")
log(by_month.to_string(index=False) + "\n")

# -----------------------------------------------------------------
# Sales by quarter
# -----------------------------------------------------------------
by_quarter = (
    df.groupby("Quarter")
      .agg(Total_Sales=("Sales", "sum"), Orders=("OrderID", "nunique"))
      .reset_index()
      .sort_values("Quarter")
)
by_quarter.to_csv("sales_by_quarter.csv", index=False)
log("=== SALES BY QUARTER ===")
log(by_quarter.to_string(index=False) + "\n")

# -----------------------------------------------------------------
# Region x Category cross-tab (bonus insight)
# -----------------------------------------------------------------
pivot = df.pivot_table(index="Region", columns="Category", values="Sales", aggfunc="sum", fill_value=0).round(2)
pivot.to_csv("region_category_pivot.csv")
log("=== SALES: REGION x CATEGORY ===")
log(pivot.to_string() + "\n")

with open("analysis_log.txt", "w") as f:
    f.write("\n".join(log_lines))

print("\nDone. See analysis_log.txt and the summary CSVs.")
