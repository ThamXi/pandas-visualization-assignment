# -------------------------------------------------------
# Basic Statistics
# -------------------------------------------------------
print("Basic Statistics:")
print(df.describe(), "\n")

# -------------------------------------------------------
# Grouping: Mean of features by Species
# -------------------------------------------------------
group_means = df.groupby("species").mean()
print("Mean values per species:")
print(group_means, "\n")

# -------------------------------------------------------
# Identify patterns or findings (printed manually)
# -------------------------------------------------------
print("Insights:")
print("- Setosa has the smallest petal measurements.")
print("- Virginica generally has the largest petal length/width.")
print("- Versicolor sits in the middle of the three species.")
