import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="Susmitha@789", # your MySQL password
    database="daily_time_sheet_2025"
)

cursor = conn.cursor()

# Execute the SQL to show all tables
cursor.execute("SHOW TABLES")

print("Tables in the database:")
for table in cursor.fetchall():
    print(table[0])

# Close connection
conn.close()
