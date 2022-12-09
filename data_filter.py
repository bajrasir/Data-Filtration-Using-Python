
import pandas as pd
import re



desired_width=320

pd.set_option('display.width', desired_width)

pd.set_option('display.max_columns',10)

excel_file_path = "C:\\Users\\uSer\\Desktop\\techmauri_scraped_futsal_data.xls"

df = pd.read_excel(excel_file_path)

df['address'] = df['address'].str.replace(r'\w+\d+.+\w$', "Kathmandu")
# df['address'] = df['address'].str.replace(r'^[A-Za-z0-9+/]+',"Kathmandu")

print(df)
# df.to_excel('C:\\Users\\uSer\\Desktop\\revised_address_futsal_data.xlsx')