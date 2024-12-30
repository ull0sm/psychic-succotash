import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,4,3,2,1]

plt.title("bar graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.bar(x,y)
plt.show()