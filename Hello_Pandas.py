import pandas as pd

# Series
sales = pd.Series([5000,7000,9000])
print(sales)

print("================================")

sales = pd.Series(
     [2500,3500,4500],
     index = ["January", "February", "March"]
)              # our own index labels.
print(sales)   

print("================================")

sales = pd.Series(
     [10,20,30,40],
     index = ["A", "B", "C", "D"]
)
print(sales["C"])   # Access value using index label.
print(sales.iloc[3])     # Access value using index position.

print("================================")

sales = {
     "Jan": 2000000,
     "Feb": 7000000,
     "Mar": 3000000
}
sales_series = pd.Series(sales) # Series from dictionary.
print(sales_series)

print("================================")

monthly_data = pd.Series(
     [1000,3000,6000],
     name = "Monthly Sales"   # Name of the Series
)
print(monthly_data)

print("================================")

# DataFrame
data = {
     "Name":["Alice", "Bob", "Charlie", "David"],
     "Age":[20,30,40,50]
}
df = pd.DataFrame(data)  # convert dictionary to DataFrame/table.
print(df)

print("================================")

data = {
     "Name":["Alice", "Bob", "Charlie", "David"],
     "Sales" :[1000,2000,3000,4000]
}
df = pd.DataFrame(data)
print(df.loc[1])  # Access row using index position.

print("================================")

