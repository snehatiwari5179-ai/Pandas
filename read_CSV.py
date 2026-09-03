import pandas as pd

pd.options.display.max_rows = 10 # Set the maximum number of rows to display in the output.

df = pd.read_csv("employees.csv")

print(df.head(3)) # Display first 3 rows of the DataFrame.
print(df.tail(8)) # Display last 8 rows of the DataFrame.
df.info()        #  shows basic DataFrame information.
usecols=["Name", "Department", "Salary" ] # Specify the columns to read from the CSV file.
print(df[usecols]) # Display the specified columns from the DataFrame.