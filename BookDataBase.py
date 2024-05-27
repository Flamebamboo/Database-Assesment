#docstring - Asyraf Books Database

#import

#constants and variables
DATABASE = "books.db"

#All functions for users to input
#1
def print_all_books():
    '''print all books '''
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * from books;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()
#2
def print_oldest_books():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * From Books ORDER BY publishing_date ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()
#3
def print_newest_books():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * From Books ORDER BY publishing_date DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()


#4
def print_horror_genre():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Horror' ORDER BY genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()

#5
def print_childrens_litreture():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Children's Literature' ORDER BY  genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()
#6
def print_fantasy_genre():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Books WHERE genre_type = 'Fantasy' ORDER BY  genre_type DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
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
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()
#8
def list_all_author():
    import sqlite3
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    sql = "SELECT author_name FROM Books;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #looop through all results here
    for books in results:
        print(books)
    #loop through all results first
    print(results)
    db.close()



#main
while True:
    user_input = input("What would you like to do. \n1.All books.\n2.Oldest books.\n3.Newest to oldest book.\n4.Oldest to Newest book.\n5.Print childrens literature.\n6.Print fantasy genre.\n7.print science fiction.\n8.list all author.\n9.Exit")
    if user_input == "1":
        print_all_books()

    elif user_input == "2":
        print_oldest_books()

    elif user_input == "3":
        print_newest_books()
        
    elif user_input == "4":
        print_horror_genre()
    
    elif user_input == "5":
        print_childrens_litreture()

    elif user_input == "6":
        print_fantasy_genre()
    elif user_input == "7":
        print_science_fiction()
    elif user_input == "8":
        list_all_author()
    elif user_input == "9":
        break