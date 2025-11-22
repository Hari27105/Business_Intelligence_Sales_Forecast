# 📊 Sales Forecasting & Business Intelligence System

> **End-to-End Data Analytics Project** demonstrating sales prediction using Machine Learning, interactive dashboards, and database management.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![ML](https://img.shields.io/badge/ML-Scikit--learn-orange)
![SQL](https://img.shields.io/badge/Database-MySQL-blue)
![PowerBI](https://img.shields.io/badge/Visualization-PowerBI-yellow)
![Streamlit](https://img.shields.io/badge/WebApp-Streamlit-red)

---

## 🎯 Project Overview

This project demonstrates a **complete data analytics workflow** from raw data to actionable insights:

✅ Data cleaning and preprocessing of **1200+ sales records**  
✅ Exploratory data analysis with statistical insights  
✅ **Linear Regression model** achieving **84% accuracy**  
✅ Interactive **Power BI dashboard** with AI-powered forecasting  
✅ **Streamlit web application** for real-time predictions  

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Programming** | Python 3.8+ |
| **Data Analysis** | Pandas, NumPy, Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn (Linear Regression) |
| **Database** | MySQL, SQLAlchemy |
| **Visualization** | Power BI, Plotly |
| **Web Framework** | Streamlit |
| **Tools** | Jupyter Notebook, Git, Excel |

---

## 📁 Project Structure

```
Business_Intelligence_Sales_Forecast/
│
├── data/
│   ├── raw_sales_data.csv          # Original dataset (1212 records)
│   └── cleaned_sales_data.csv      # Processed data (1181 records)
│
├── notebooks/
│   ├── 01_data_cleaning.py         # Data cleaning & preprocessing
│   ├── 02_eda_analysis.py          # Exploratory data analysis
│   └── 03_ml_model.py              # Machine learning model
│
├── sql/
│   ├── create_database.sql         # Database schema
│   └── analysis_queries.sql        # SQL queries for analysis
│
├── models/
│   └── sales_forecast_model.pkl    # Trained ML model
│
├── app/
│   └── streamlit_app.py            # Interactive web application
│
├── powerbi/
│   └── [Power BI dashboard file]   # .pbix file (create manually)
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Quick Start Guide

### 1️⃣ Installation

```bash
# Clone the repository
git clone https://github.com/Hari27105/Business_Intelligence_Sales_Forecast.git
cd Business_Intelligence_Sales_Forecast

# Install required packages
pip install -r requirements.txt
```

### 2️⃣ Run Data Analysis

```bash
# Run data cleaning
python notebooks/01_data_cleaning.py

# Run exploratory data analysis
python notebooks/02_eda_analysis.py

# Train ML model
python notebooks/03_ml_model.py
```

### 3️⃣ Launch Web Application

```bash
cd app
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### 4️⃣ Setup MySQL Database (Optional)

```bash
# Login to MySQL
mysql -u root -p

# Run the SQL script
source sql/create_database.sql
```

### 5️⃣ Create Power BI Dashboard

1. Open Power BI Desktop
2. Import `data/cleaned_sales_data.csv`
3. Create visualizations as per project guide
4. Save as `sales_dashboard.pbix`

---

## 📊 Key Features

### 🔹 Data Pipeline
- **Automated data cleaning** (handles missing values, duplicates, outliers)
- **Feature engineering** (time-based features, profit margins)
- **Statistical analysis** using IQR method for outlier detection

### 🔹 Machine Learning
- **Linear Regression model** for revenue forecasting
- **84.41% accuracy** (R² Score: 0.8441)
- Model evaluation with RMSE, MAE, and R² metrics
- Feature importance analysis

### 🔹 Visualizations
- **Monthly revenue trends** with time-series analysis
- **Product performance analysis** (top sellers, revenue distribution)
- **Correlation heatmaps** for feature relationships
- **Interactive Power BI dashboard** with drill-down capabilities

### 🔹 Web Application
- **Real-time predictions** based on user inputs
- **Interactive charts** using Plotly
- **Dashboard analytics** with key metrics
- **Data exploration** with downloadable reports

---

## 📈 Model Performance

| Metric | Training Set | Testing Set |
|--------|--------------|-------------|
| **R² Score** | 0.8547 (85.47%) | 0.8441 (84.41%) |
| **RMSE** | ₹842,167.11 | ₹871,507.06 |
| **MAE** | ₹628,901.45 | ₹651,747.69 |

**Feature Importance:**
1. Units_Sold: 22,141.20
2. Quarter: 11,597.81
3. Unit_Price: 109.38
4. Month: -21,055.93

---

## 📊 Sample Insights

### Total Revenue
**₹3,137,393,593** across 1181 transactions

### Top 5 Products by Revenue
1. **Laptop**: ₹565M
2. **Graphics Card**: ₹461M
3. **Camera**: ₹458M
4. **Printer**: ₹341M
5. **Smartphone**: ₹331M

### Seasonal Trends
- **Highest sales**: November-December (holiday season)
- **Average profit margin**: 40%
- **Peak quarter**: Q4 (October-December)

---

## 💼 Business Applications

This project demonstrates skills directly applicable to:

✅ **Data Analyst roles** - Data cleaning, EDA, visualization  
✅ **Business Intelligence** - Dashboard creation, insights generation  
✅ **Machine Learning** - Predictive modeling, model evaluation  
✅ **Database Management** - SQL queries, data warehousing  

---

## 🎓 Skills Demonstrated

| Skill Category | Specific Skills |
|----------------|-----------------|
| **Python Programming** | Pandas, NumPy, data manipulation |
| **Data Analysis** | EDA, statistical analysis, feature engineering |
| **Machine Learning** | Regression, model training, evaluation |
| **SQL** | Database design, complex queries, optimization |
| **Visualization** | Power BI, Matplotlib, Seaborn, Plotly |
| **Web Development** | Streamlit, interactive dashboards |
| **Version Control** | Git, GitHub |

---

## 📝 How to Use This for Job Applications

### Resume Entry Example

**Sales Forecasting & Business Intelligence System** | Python, SQL, ML, Power BI | Nov 2024

- Developed an end-to-end sales forecasting system using Python, integrating data cleaning, exploratory analysis, and predictive modeling with Linear Regression achieving **84% accuracy** (R² score of 0.84)
- Designed and implemented a **MySQL database** for storing 1200+ sales transactions; wrote optimized SQL queries for data extraction and analysis
- Built an **interactive Power BI dashboard** with 8+ visualizations including monthly trends, product analysis, and AI-powered 12-month sales forecast
- Created a **Streamlit web application** for real-time revenue prediction, enabling business users to make data-driven decisions
- Applied **feature engineering** techniques and **statistical methods** (IQR for outlier detection) to improve data quality and model performance

**Tech Stack:** Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn), MySQL, Power BI, Streamlit, Git

---

## 👤 Author

**Hari Prasad Kadu**

📧 **Email:** kaduhariprasad@gmail.com  
💼 **LinkedIn:** [hariprasad-kadu-855382314](https://linkedin.com/in/hariprasad-kadu-855382314)  
🐱 **GitHub:** [Hari27105](https://github.com/Hari27105)

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 🙏 Acknowledgments

- Dataset: Synthetically generated for educational purposes
- Inspired by real-world business intelligence use cases
- Built as a portfolio project for data analyst job applications

---

## 🌟 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Implement time-series forecasting (ARIMA, Prophet)
- [ ] Add customer segmentation analysis
- [ ] Create automated email reports
- [ ] Deploy as cloud application (AWS/Azure)
- [ ] Add A/B testing framework

---

## 📞 Contact for Collaboration

Interested in collaborating or have questions? Feel free to reach out!

**Email:** kaduhariprasad@gmail.com  
**LinkedIn:** [Connect with me](https://linkedin.com/in/hariprasad-kadu-855382314)

---

⭐ **If you found this project helpful, please give it a star!** ⭐

---

*Last Updated: November 2024*
