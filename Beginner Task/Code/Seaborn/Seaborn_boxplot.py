import seaborn as sns
import matplotlib.pyplot as plt

marks = [50, 60, 70, 80, 90, 75, 65, 85, 55]

sns.boxplot(y=marks)
plt.title("Box Plot of Marks")
plt.show()
