import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
create_query = "CREATE TABLE IF NOT EXISTS users(userid TEXT,password TEXT)"
cursor.execute(create_query)
connection.commit()
connection.close()