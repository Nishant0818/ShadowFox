import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry"]
marks = [85, 78, 92]

plt.bar(subjects, marks, color="green")
plt.title("Marks in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
