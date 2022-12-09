import mysql.connector
import xlrd

# Connecting to the database
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="techmauri")
cur = conn.cursor()

# location of the excel sheet
loc = "C:\\Users\\uSer\\Desktop\\techmauri_scraped_futsal_data.xls"

# Reading Excel Sheet
a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
# query to insert in the database
query = "insert into techmauri_scraped_futsal_datas(name,rating,review,address,phone,comment)values(%s,%s,%s,%s,%s,%s)"
# looping through the Excel sheet to retrieve the data
for i in range(1, sheet.nrows):
    name = sheet.cell(i, 0).value
    rating = sheet.cell(i, 1).value
    review = sheet.cell(i, 2).value
    address = sheet.cell(i, 3).value
    phone = sheet.cell(i, 4).value
    comment = sheet.cell(i, 5).value

    values = (name, rating, review, address, phone, comment)
    # executing the query
    cur.execute(query, values)

conn.commit()
conn.close()
