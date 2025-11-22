# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('data/cleaned_sales_data.csv')

print("🤖 BUILDING SALES FORECASTING MODEL\n")

# Prepare data for ML
X = df[['Units_Sold', 'Unit_Price', 'Month', 'Quarter']]
y = df['Revenue']

print("📊 Feature Matrix Shape:", X.shape)
print("📊 Target Vector Shape:", y.shape)

# Split data (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\n📚 Training Set: {len(X_train)} samples")
print(f"🧪 Testing Set: {len(X_test)} samples")

# Create and train model
print("\n🔄 Training the model...")
model = LinearRegression()
model.fit(X_train, y_train)
print("✅ Model training completed!")

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate
print("\n" + "="*50)
print("📈 MODEL PERFORMANCE METRICS")
print("="*50)

train_r2 = r2_score(y_train, y_pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
train_mae = mean_absolute_error(y_train, y_pred_train)

print(f"\n🎯 Training Set:")
print(f"  R² Score: {train_r2:.4f} ({train_r2*100:.2f}% accuracy)")
print(f"  RMSE: ₹{train_rmse:.2f}")
print(f"  MAE: ₹{train_mae:.2f}")

test_r2 = r2_score(y_test, y_pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
test_mae = mean_absolute_error(y_test, y_pred_test)

print(f"\n🎯 Testing Set:")
print(f"  R² Score: {test_r2:.4f} ({test_r2*100:.2f}% accuracy)")
print(f"  RMSE: ₹{test_rmse:.2f}")
print(f"  MAE: ₹{test_mae:.2f}")

# Feature importance
print("\n" + "="*50)
print("📊 FEATURE IMPORTANCE")
print("="*50)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values('Coefficient', ascending=False)
print(feature_importance)

# Save model
model_path = 'models/sales_forecast_model.pkl'
joblib.dump(model, model_path)
print(f"\n✅ Model saved to: {model_path}")

# Visualization
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_test, alpha=0.6, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Revenue (₹)', fontsize=12)
plt.ylabel('Predicted Revenue (₹)', fontsize=12)
plt.title('Actual vs Predicted Revenue', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
residuals = y_test - y_pred_test
plt.hist(residuals, bins=30, color='coral', edgecolor='black', alpha=0.7)
plt.xlabel('Residuals (₹)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Residuals Distribution', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('data/model_performance.png', dpi=300, bbox_inches='tight')

plt.show()

print("\n✅ Machine Learning model completed!")