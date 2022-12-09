import mysql.connector


# Connecting to the database
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="techmauri")
cur = conn.cursor()

update_query = "update techmauri_scraped_futsal_datas SET address = 'Kathmandu' WHERE address != 'Kathmandu'"

try:
    cur.execute(update_query)
    conn.commit()
    print("Updated Successfully!")

except:
    print("Unable to update data!")

    conn.close()
