# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Load cleaned data
df = pd.read_csv('data/cleaned_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("📊 EXPLORATORY DATA ANALYSIS\n")

# 1. Overall Sales Metrics
print("="*50)
print("📈 KEY METRICS")
print("="*50)
print(f"Total Revenue: ₹{df['Revenue'].sum():,.2f}")
print(f"Average Revenue per Transaction: ₹{df['Revenue'].mean():,.2f}")
print(f"Total Units Sold: {df['Units_Sold'].sum():,.0f}")
print(f"Number of Products: {df['Product'].nunique()}")
print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")

# 2. Top 5 Products by Revenue
print("\n" + "="*50)
print("🏆 TOP 5 PRODUCTS BY REVENUE")
print("="*50)
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head()
print(top_products)

# 3. Monthly Revenue Trend
monthly_revenue = df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()
print("\n" + "="*50)
print("📅 MONTHLY REVENUE TREND")
print("="*50)
print(monthly_revenue)

# Visualizations
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
monthly_revenue['Year_Month'] = monthly_revenue['Year'].astype(str) + '-' + monthly_revenue['Month'].astype(str).str.zfill(2)
plt.plot(range(len(monthly_revenue)), monthly_revenue['Revenue'], marker='o', linewidth=2, markersize=8)
plt.title('Monthly Revenue Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (₹)', fontsize=12)
plt.xticks(range(len(monthly_revenue)), monthly_revenue['Year_Month'], rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.subplot(1, 2, 2)
top_products.plot(kind='barh', color='steelblue')
plt.title('Top 5 Products by Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Revenue (₹)', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('data/eda_analysis.png', dpi=300, bbox_inches='tight')


print("\n✅ EDA completed! Charts saved.")