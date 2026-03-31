import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 35, 33, 31]

plt.plot(days, temperature, color="blue")
plt.title("Temperature Over Days")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
