
plt.figure()
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.scatter(subset["sepal length (cm)"],
                subset["petal length (cm)"],
                label=species)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.legend()
plt.show()
