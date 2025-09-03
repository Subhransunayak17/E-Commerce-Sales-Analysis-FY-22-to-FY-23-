import pandas as pd
from sqlalchemy import create_engine

# Database connection
conn_string = "postgresql://postgres:12345@localhost:1176/ecommerce"
db = create_engine(conn_string)
conn = db.connect()

# File paths
csv_path = r"C:\Users\subhr\OneDrive\Desktop\Ecommerce\us_state_long_lat_codes.csv"
excel_path = r"C:\Users\subhr\OneDrive\Desktop\Ecommerce\ecommerce_data_excel.xlsx"

# Insert CSV file
df_csv = pd.read_csv(csv_path)
df_csv.to_sql("us_state_long_lat_codes", con=conn, if_exists="replace", index=False)
print("✅ Inserted CSV as table 'us_state_long_lat_codes'")

# Insert Excel sheet (using correct sheet name 'ecommerce_data')
df_excel = pd.read_excel(excel_path, sheet_name="ecommerce_data", engine="openpyxl")
df_excel.to_sql("ecommerce_data", con=conn, if_exists="replace", index=False)
print("✅ Inserted Excel sheet 'ecommerce_data' as table 'ecommerce_data'")

conn.close()
