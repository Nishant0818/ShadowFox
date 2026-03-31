import seaborn as sns
import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry"]
marks = [85, 78, 92]

sns.barplot(x=subjects, y=marks)
plt.title("Marks in Subjects")
plt.show()
