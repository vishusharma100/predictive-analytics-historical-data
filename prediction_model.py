"""
Predictive Analytics Using Historical Data
Sales forecasting using Linear Regression.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("dataset/historical_sales.csv", parse_dates=["Date"])
df = df.drop_duplicates().dropna(subset=["Date", "Sales"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["TimeIndex"] = np.arange(len(df))

features = ["Year", "Month", "TimeIndex"]
X, y = df[features], df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, shuffle=False
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.4f}")

future_dates = pd.date_range(
    df["Date"].max() + pd.offsets.MonthBegin(1),
    periods=12, freq="MS"
)
future = pd.DataFrame({"Date": future_dates})
future["Year"] = future["Date"].dt.year
future["Month"] = future["Date"].dt.month
future["TimeIndex"] = np.arange(len(df), len(df) + 12)
future["Predicted_Sales"] = model.predict(future[features])
future.to_csv("dataset/future_sales_forecast.csv", index=False)
print(future)
