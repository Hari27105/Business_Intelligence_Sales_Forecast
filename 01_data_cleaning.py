# Import necessary libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Load the raw dataset
df = pd.read_csv('data/raw_sales_data.csv')


print("📊 Original Dataset Shape:", df.shape)
print("\n📋 First 5 rows:")
print(df.head())

# Check for missing values
print("\n❌ Missing Values:")
print(df.isnull().sum())

# Data Cleaning Steps
# 1. Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 2. Remove duplicate rows
df = df.drop_duplicates()
print(f"\n✅ After removing duplicates: {df.shape[0]} rows")

# 3. Handle missing values
df['Units_Sold'] = df['Units_Sold'].fillna(df['Units_Sold'].mean())
df['Unit_Price'] = df['Unit_Price'].fillna(df['Unit_Price'].mean())
df['Revenue'] = df['Revenue'].fillna(df['Revenue'].mean())

# 4. Feature Engineering - Extract date components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()
df['Quarter'] = df['Date'].dt.quarter
df['Day_of_Week'] = df['Date'].dt.day_name()

# 5. Calculate additional metrics
df['Profit_Margin'] = (df['Revenue'] - (df['Units_Sold'] * df['Unit_Price'] * 0.6)) / df['Revenue'] * 100

# 6. Remove outliers using IQR method
Q1 = df['Revenue'].quantile(0.25)
Q3 = df['Revenue'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Revenue'] >= Q1 - 1.5*IQR) & (df['Revenue'] <= Q3 + 1.5*IQR)]

print(f"\n✅ After removing outliers: {df.shape[0]} rows")

# Save cleaned data
df.to_csv('data/cleaned_sales_data.csv', index=False)

print("\n✅ Cleaned data saved successfully!")

# Display final dataset info
print("\n📊 Cleaned Dataset Info:")
print(df.info())
print("\n📈 Statistical Summary:")
print(df.describe())