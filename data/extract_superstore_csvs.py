import pandas as pd

# Load the Excel file once
file_path = "Sample - Superstore.xls"
df = pd.read_excel(file_path, sheet_name="Orders")
print(df.columns.tolist())  # Temporary check to list all column names

# --- Extract Customers ---
customer_df = df[["Customer ID", "Customer Name"]].drop_duplicates()
customer_df.to_csv("customers.csv", index=False)
print("customers.csv file created")

# --- Extract Location Info ---
location_df = df[["Postal Code", "City", "State", "Region"]].drop_duplicates()
location_df.to_csv("location.csv", index=False)
print("location.csv file created")

# --- Extract Orders ---
orders_df = df[["Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
                "Customer ID", "Segment", "Postal Code", "Product ID",
                "Sales", "Quantity", "Discount", "Profit"]]
orders_df.to_csv("orders.csv", index=False)
print("orders.csv file created")

# --- Extract Products ---
products_df = df[["Product ID", "Product Name", "Category", "Sub-Category"]].drop_duplicates()
products_df.to_csv("products.csv", index=False)
print("products.csv file created")