import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

sns.set(style="whitegrid")

sns.scatterplot(x= "total_bill",y= "tip",data = tips,hue="sex")

plt.title("asthetic functions")
plt.xlabel("total bill")
plt.ylabel("tip")

plt.show()