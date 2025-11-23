
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# -------------------------------------------------------
# Load Dataset with Error Handling
# -------------------------------------------------------
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    df["species"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    print("Dataset loaded successfully.\n")

except Exception as e:
    print("Error loading dataset:", e)

# -------------------------------------------------------
# Display first rows
# -------------------------------------------------------
print("First 5 rows:")
print(df.head(), "\n")

# -------------------------------------------------------
# Inspect data structure
# -------------------------------------------------------
print("Data Types:")
print(df.dtypes, "\n")

print("Missing Values:")
print(df.isnull().sum(), "\n")

# -------------------------------------------------------
# Cleaning (Iris dataset has no missing values, but code is shown)
# -------------------------------------------------------
df = df.dropna()   # remove missing rows if any
