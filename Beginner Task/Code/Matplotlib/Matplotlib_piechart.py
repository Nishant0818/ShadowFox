import matplotlib.pyplot as plt

labels = ["Product A", "Product B", "Product C"]
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Market Share Distribution")
plt.show()
