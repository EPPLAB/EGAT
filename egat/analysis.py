
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def calculate_correlation(df, columns):
    return df[columns].corr()

def run_regression(df, target, features):
    X = df[features]
    y = df[target]
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    return model, r2, rmse
