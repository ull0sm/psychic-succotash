import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset from the Excel file
df = pd.read_excel("pyexp7.xlsx")  # Load the Excel file from the same folder

# Display the first few rows of the dataset
print(df.head())

# Set Seaborn style
sns.set_style("whitegrid", rc={"lines.linewidth": 2.5, "grid.color": "red", "xtick.color": "blue"})

# Create a scatter plot
sns.scatterplot(x="Total_bill", y="Tip", hue="Sex", data=df)
# Save the plot as an image file
plt.savefig("scatter_plot.png")

# Display the plot
plt.show()
