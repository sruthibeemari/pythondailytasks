import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ----------------------------
# LOAD DATASET
# ----------------------------

data = pd.read_csv("kc_house_data.csv")

# Remove missing values
data = data.dropna()

# Drop unnecessary columns
data = data.drop(["id", "date"], axis=1)

# Features and target
X = data.drop("price", axis=1)
y = data["price"]

# ----------------------------
# SPLIT DATA
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------
# SCALE DATA
# ----------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =====================================================
# ANN MODEL
# =====================================================

print("\n========== ANN MODEL ==========\n")

ann_model = MLPRegressor(
    hidden_layer_sizes=(128, 64, 32),
    activation='relu',
    max_iter=500,
    random_state=42
)

# Train ANN
ann_model.fit(X_train_scaled, y_train)

# Predict
ann_prediction = ann_model.predict(X_test_scaled)

# Metrics
ann_mae = mean_absolute_error(y_test, ann_prediction)

ann_rmse = mean_squared_error(
    y_test,
    ann_prediction
) ** 0.5

ann_r2 = r2_score(y_test, ann_prediction)

# Results
print("ANN MAE:", ann_mae)

print("ANN RMSE:", ann_rmse)

print("ANN Accuracy (R2 Score):", ann_r2)

print("\nANN Sample Prediction")

print("Predicted Price:", ann_prediction[0])

print("Actual Price:", y_test.iloc[0])

# =====================================================
# RANDOM FOREST MODEL
# =====================================================

print("\n========== RANDOM FOREST MODEL ==========\n")

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train RF
rf_model.fit(X_train, y_train)

# Predict
rf_prediction = rf_model.predict(X_test)

# Metrics
rf_mae = mean_absolute_error(y_test, rf_prediction)

rf_rmse = mean_squared_error(
    y_test,
    rf_prediction
) ** 0.5

rf_r2 = r2_score(y_test, rf_prediction)

# Results
print("Random Forest MAE:", rf_mae)

print("Random Forest RMSE:", rf_rmse)

print("Random Forest Accuracy (R2 Score):", rf_r2)

print("\nRandom Forest Sample Prediction")

print("Predicted Price:", rf_prediction[0])

print("Actual Price:", y_test.iloc[0])