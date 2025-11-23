
plt.figure()
plt.bar(group_means.index, group_means["petal length (cm)"])
plt.xlabel("Species")
plt.ylabel("Mean Petal Length (cm)")
plt.title("Bar Chart: Average Petal Length per Species")
plt.show()
