import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [5,4,3,2,1]
y1 = np.sqrt(y)
y2 = np.square(y)

plt.title("line graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x,y,x,y1,x,y2)
plt.show()