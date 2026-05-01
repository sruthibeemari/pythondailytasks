#========================================================================
#Importing libraries
#========================================================================

import numpy as np
import pandas as pd

#========================================================================
#Load Dataset
#========================================================================
dataset=pd.read_csv('kc_house_data.csv')
print(dataset.head())

# ============================================================
# Convert price into categories (classification problem)
# ============================================================
#0=low, 1=Medium, 2=High
dataset['price_category']=pd.cut(dataset['price'],bins=3,labels=[0,1,2])

# ============================================================
# Features (X) and Target (y)
# ============================================================
X=dataset[['bedrooms','bathrooms','sqft_living','sqft_lot','floors',
             'condition','grade','sqft_basement','yr_built','yr_renovated']].values
y=dataset['price_category'].values

print('-'*80)
print(f'Shape of X:{X.shape}')
print(f'Shape of y:{y.shape}')

# ============================================================
# Train-Test Split
# ============================================================


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=0
)

# ============================================================
# Feature Scaling (needed for some models)
# ============================================================

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train_scaled=sc.fit_transform(X_train)
X_test_scaled=sc.transform(X_test)

# ============================================================
# Evaluation Function
# ============================================================


from sklearn.metrics import accuracy_score

def run_model(model, use_scaled=False):
    if use_scaled:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    print(model)
    print('\n' + '-'*20 + 'Accuracy Score on the Test set' + '-'*20)
    print("{:.0%}".format(accuracy_score(y_test, y_pred)))



# ============================================================
# 1. Support Vector Machine (SVC)
# ============================================================
from sklearn.svm import SVC
run_model(SVC(), use_scaled=True)

# ============================================================
# 2. Logistic Regression
# ============================================================
from sklearn.linear_model import LogisticRegression
run_model(LogisticRegression(max_iter=1000), use_scaled=True)

# ============================================================
# 3. Naive Bayes
# ============================================================
from sklearn.naive_bayes import GaussianNB
run_model(GaussianNB())

# ============================================================
# 4. Decision Tree
# ============================================================
from sklearn.tree import DecisionTreeClassifier
run_model(DecisionTreeClassifier())

# ============================================================
# 5. Random Forest
# ============================================================
from sklearn.ensemble import RandomForestClassifier
run_model(RandomForestClassifier())

# ============================================================
# 6. K-Nearest Neighbors (KNN)
# ============================================================
from sklearn.neighbors import KNeighborsClassifier
run_model(KNeighborsClassifier(), use_scaled=True)

# ============================================================
# 7. Gradient Boosting
# ============================================================
from sklearn.ensemble import GradientBoostingClassifier
run_model(GradientBoostingClassifier())
