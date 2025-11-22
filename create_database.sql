-- Create Database
CREATE DATABASE IF NOT EXISTS sales_forecast_db;
USE sales_forecast_db;

-- Create sales_data table
CREATE TABLE IF NOT EXISTS sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE NOT NULL,
    Product VARCHAR(100),
    Units_Sold INT,
    Unit_Price DECIMAL(10, 2),
    Revenue DECIMAL(12, 2),
    Year INT,
    Month INT,
    Month_Name VARCHAR(20),
    Quarter INT,
    Day_of_Week VARCHAR(20),
    Profit_Margin DECIMAL(5, 2),
    INDEX idx_date (Date),
    INDEX idx_product (Product)
);

-- Show table structure
DESCRIBE sales_data;
