import matplotlib.pyplot as plt

marks = [50, 60, 70, 80, 90, 75, 65, 85, 55]

plt.hist(marks, color="purple", bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
