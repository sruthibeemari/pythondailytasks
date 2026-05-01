#========================================================================
# Importing libraries
#========================================================================
import numpy as np
import pandas as pd

#========================================================================
# Load Dataset
#========================================================================
dataset = pd.read_csv('kc_house_data.csv')
print(dataset.head())

#========================================================================
# Features (X) and Target (y)
#========================================================================
X = dataset[['bedrooms','bathrooms','sqft_living','sqft_lot','floors',
             'condition','grade','sqft_basement','yr_built','yr_renovated']].values

y = dataset['price'].values   # Continuous target (REGRESSION)

print('-'*80)
print(f'Shape of X: {X.shape}')
print(f'Shape of y: {y.shape}')

#========================================================================
# Train-Test Split
#========================================================================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

#========================================================================
# Feature Scaling (needed for some models)
#========================================================================
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

#========================================================================
# Evaluation Function (REGRESSION METRICS)
#========================================================================
from sklearn.metrics import mean_squared_error, r2_score

def run_model(model, use_scaled=False):
    if use_scaled:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    print(model)
    print('\n' + '-'*20 + 'Regression Metrics' + '-'*20)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("MSE :", mse)
    print("RMSE:", rmse)
    print("R2 Score:", r2)


#========================================================================
# 1. Support Vector Regression (SVR)
#========================================================================
from sklearn.svm import SVR
run_model(SVR(), use_scaled=True)

#========================================================================
# 2. Decision Tree Regressor
#========================================================================
from sklearn.tree import DecisionTreeRegressor
run_model(DecisionTreeRegressor())

#========================================================================
# 3. Random Forest Regressor
#========================================================================
from sklearn.ensemble import RandomForestRegressor
run_model(RandomForestRegressor())

#========================================================================
# 4. K-Nearest Neighbors Regressor
#========================================================================
from sklearn.neighbors import KNeighborsRegressor
run_model(KNeighborsRegressor(), use_scaled=True)

#========================================================================
# 5. Gradient Boosting Regressor
#========================================================================
from sklearn.ensemble import GradientBoostingRegressor
run_model(GradientBoostingRegressor())

#========================================================================
# 6. Linear Regression
#========================================================================
from sklearn.linear_model import LinearRegression
run_model(LinearRegression())

#========================================================================
# 7. Extra Trees Regressor
#========================================================================
from sklearn.ensemble import ExtraTreesRegressor
run_model(ExtraTreesRegressor())