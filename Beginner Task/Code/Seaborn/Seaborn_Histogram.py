import seaborn as sns
import matplotlib.pyplot as plt

marks = [50, 60, 70, 80, 90, 75, 65, 85, 55]

sns.histplot(marks)
plt.title("Distribution of Marks")
plt.show()
