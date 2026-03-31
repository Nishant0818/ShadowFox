import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 70, 80]

plt.scatter(hours, marks, color="red")
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
