import seaborn as sns
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 35, 33, 31]

sns.lineplot(x=days, y=temperature)
plt.title("Temperature Over Days")
plt.show()
