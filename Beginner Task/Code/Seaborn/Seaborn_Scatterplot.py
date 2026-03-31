import seaborn as sns
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 70, 80]

sns.scatterplot(x=hours, y=marks)
plt.title("Hours Studied vs Marks")
plt.show()
