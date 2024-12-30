import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = ["monday","tuesday","wednesday","thursday","friday"]
plt.title("pie graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.pie(x,labels=y)
plt.show()