import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,3,2,7,5,1,7,4,6,2,1,7,4,2]

plt.title("histogram graph")
plt.xlabel("value")
plt.ylabel("frequency")

plt.hist(x,bins=5)
plt.show()