
from sklearn.ensemble import RandomForestRegressor

def calculate_feature_importance(df, target, features):
    model = RandomForestRegressor()
    model.fit(df[features], df[target])
    return dict(zip(features, model.feature_importances_))
