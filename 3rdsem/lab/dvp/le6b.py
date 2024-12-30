import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, linestyle='--', marker='o', label='Line with markers')

plt.title('Formatted Linear Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.show()