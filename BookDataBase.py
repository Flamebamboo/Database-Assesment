#docstring - Asyraf Books Database
from tabulate import tabulate
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
#All functions for users to input
#using mixed of tabulate format of "rouded_grid" and fancy_grid

def print_all_books():
    '''print all books '''
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * from books;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["ID", "Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="rounded_grid"))

    db.close()

#2
def print_oldest_books():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * From Books ORDER BY publishing_date ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["ID","Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="fancy_grid"))
    db.close()
#3
def print_newest_books():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * From Books ORDER BY publishing_date DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["ID", "Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="rounded_grid",))

    db.close()


#4
def print_horror_genre():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Horror' ORDER BY genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["ID","Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="rounded_grid"))
    db.close()

#5
def print_childrens_literature():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Children''s Literature' ORDER BY genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["ID","Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="fancy_grid"))
    db.close()
#6
def print_fantasy_genre():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Fantasy' ORDER BY  genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["ID","Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="fancy_grid"))
    db.close()
#7
def print_science_fiction():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Science Fiction' ORDER BY  genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    print(tabulate(results, headers=["ID","Title", "Author", "Publishing Date", "Genre", "Summary"], tablefmt="rounded_grid"))
    db.close()
#8
def list_all_author():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT author_name FROM Books;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results, headers=["Name"], tablefmt="rounded_grid"))
    db.close()

def add_data():
    """Add a new book to the database."""
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()

    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    publishing_date = input("Enter publishing date (Year-month-day): ")
    genre = input("Enter genre: ")
    summary = input("Enter summary: ")    
      
    sql = "INSERT INTO Books (book_name, author_name, publishing_date, genre_type, summary) VALUES (?, ?, ?, ?, ?);"
    cursor.execute(sql, (book_title, author_name, publishing_date, genre, summary))
    db.commit()

def remove_data():
    '''Removing data from the current database'''
    book_id = input("Enter the ID of the book to remove")

    sql = "DELETE FROM Books WHERE id = ?;"
    cursor.execute(sql, (book_id,))
    db.commit()

#main
while True:

    #giving the user options to choose from
    user_input = input("What would you like to do. \n1.All books.\n2.Oldest books.\n3.Newest to oldest book.\n4.Oldest to Newest book.\n5.Print childrens literature.\n6.Print fantasy genre.\n7.print science fiction.\n8.list all author.\n9.add data.\n10.remove data.\n11.edit.\nPrompt here: ")
   #printing all book with rounded_grid format
    if user_input == "1":
        print_all_books()
    #printing books according to the publishing date oldest to newest in fancy_grid format
    elif user_input == "2":
        print_oldest_books()
    #printing books according to the publishing date newest to oldest in rounded_grid format
    elif user_input == "3":
        print_newest_books()
    #printing all horror genre sort by decending order in rounded_grid format
    elif user_input == "4":
        print_horror_genre()
    #printing all children literature genre by decending order in fancy_grid format
    elif user_input == "5":
        print_childrens_literature()
    #printing all fantasy genre by decending order in fancy_grid format
    elif user_input == "6":
        print_fantasy_genre()
    #printing  all science fiction books by decending order in fancy_grid format
    elif user_input == "7":
        print_science_fiction()
    #listing all author in verticle nicely with rounded_grid format
    elif user_input == "8":
        list_all_author()
    elif user_input == "9":
        add_data()
    elif user_input == "10":
        remove_data()
    #  elif user_input == "11":
    #     edit_data()
    else:
        print("That is not an option")