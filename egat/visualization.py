
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_scatter(df, x_col, y_col, save_path):
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(f"{x_col} vs {y_col}")
    plt.savefig(save_path)
    plt.close()

def plot_feature_importance(importance_dict, save_path):
    items = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)
    labels, values = zip(*items)
    plt.figure(figsize=(8,6))
    sns.barplot(x=list(values), y=list(labels))
    plt.title("Feature Importance")
    plt.savefig(save_path)
    plt.close()
