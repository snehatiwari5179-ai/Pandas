import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("Emp.json")
print(df)

print(df.describe())     # Gives statistical summary of the DataFrame.

print(df.corr(numeric_only=True))  # Gives correlation between numeric columns of the DataFrame.

df["Salary"].plot(kind="bar") # Plots the Salary column of the DataFrame using a bar chart.
plt.show()

df.plot(kind="scatter", x="Experience", y="Salary")
plt.show()     # Plots a scatter plot of Experience vs Salary columns of the DataFrame.

df.plot(kind="line",x="Employee_ID", y="Salary")
plt.show()     # Plots a line chart of Employee_ID vs Salary columns of the DataFrame.

df["Salary"].plot(kind="hist") # Plots a histogram of the Salary column of the DataFrame.
plt.show()
