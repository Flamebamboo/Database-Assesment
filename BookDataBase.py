#docstring - Asyraf Books Database

#import

#constants and variables
DATABASE = "books.db"

#functions 


#main code
import sqlite3
db = sqlite3.connect("books.db")
cursor = db.cursor()
sql = "SELECT * from books;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
