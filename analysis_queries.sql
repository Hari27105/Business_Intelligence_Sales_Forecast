-- Sample SQL Queries for Analysis

-- 1. Total Revenue
SELECT SUM(Revenue) AS Total_Revenue FROM sales_data;

-- 2. Monthly Revenue Trend
SELECT Year, Month, Month_Name, SUM(Revenue) AS Monthly_Revenue
FROM sales_data
GROUP BY Year, Month, Month_Name
ORDER BY Year, Month;

-- 3. Top 5 Products by Revenue
SELECT Product, SUM(Revenue) AS Total_Revenue, SUM(Units_Sold) AS Total_Units
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;

-- 4. Quarterly Performance
SELECT Year, Quarter, 
       SUM(Revenue) AS Quarterly_Revenue,
       AVG(Profit_Margin) AS Avg_Profit_Margin
FROM sales_data
GROUP BY Year, Quarter
ORDER BY Year, Quarter;

-- 5. Product Performance Matrix
SELECT Product,
       COUNT(*) AS Transaction_Count,
       SUM(Units_Sold) AS Total_Units,
       SUM(Revenue) AS Total_Revenue,
       AVG(Revenue) AS Avg_Revenue,
       AVG(Profit_Margin) AS Avg_Profit_Margin
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC;

-- 6. Day of Week Analysis
SELECT Day_of_Week,
       SUM(Revenue) AS Total_Revenue,
       COUNT(*) AS Transaction_Count
FROM sales_data
GROUP BY Day_of_Week
ORDER BY Total_Revenue DESC;

-- 7. Year-over-Year Comparison
SELECT Year,
       SUM(Revenue) AS Annual_Revenue,
       SUM(Units_Sold) AS Annual_Units,
       AVG(Profit_Margin) AS Avg_Margin
FROM sales_data
GROUP BY Year
ORDER BY Year;
