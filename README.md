# Predictive Analytics Using Historical Data

## Overview
A complete beginner-friendly predictive analytics project that uses historical monthly sales data to predict future sales.

## Objectives
- Clean and preprocess historical data
- Analyze sales trends
- Build a regression model
- Evaluate model performance
- Forecast the next 12 months
- Visualize actual vs predicted values

## Dataset
`dataset/historical_sales.csv` contains 48 months of illustrative historical sales data from 2022–2025.

## Methodology
1. Load historical sales data
2. Remove duplicates and missing values
3. Extract Year and Month from Date
4. Create a TimeIndex feature
5. Split data chronologically into training and testing sets
6. Train Linear Regression
7. Evaluate with MAE, RMSE and R²
8. Forecast the next 12 months

## Model Results
- MAE: 831.23
- RMSE: 1029.93
- R² Score: -0.1746

> Metrics are based on the included illustrative dataset and may change if the dataset is replaced.

## Project Structure
```text
predictive-analytics-historical-data/
├── dataset/
│   ├── historical_sales.csv
│   └── future_sales_forecast.csv
├── notebooks/
│   └── predictive_analytics.ipynb
├── src/
│   └── prediction_model.py
├── graphs/
│   ├── historical_trend.png
│   ├── actual_vs_predicted.png
│   └── future_forecast.png
├── model_metrics.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook
```
Open `notebooks/predictive_analytics.ipynb` and run the cells.

## Technologies
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Jupyter Notebook.

## Skills Demonstrated
Predictive modeling, data preprocessing, regression, time/trend analysis, model evaluation and data visualization.

## Future Improvements
- Compare Random Forest Regression with Linear Regression
- Add lag and rolling-average features
- Try ARIMA/Prophet-style time-series approaches
- Build an interactive Power BI dashboard
