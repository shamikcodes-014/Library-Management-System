def first():

    import sqlite3
    from tabulate import tabulate

    conn = sqlite3.connect('Library.sqlite')
    cur=conn.cursor()

    cur.executescript('''

    DROP TABLE IF EXISTS Main;

    CREATE TABLE Main (
        Book_Name TEXT UNIQUE,
        Author TEXT,
        Quantity INTEGER,
        Book_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
        )    
    ''')

    Book_name=input("Enter Book name to be added to stock ")
    Author_name=input("Enter the author name ")
    Quantity=int(input("Enter the quantity "))

    cur.execute('''INSERT INTO Main (Book_name, Author, Quantity) VALUES (?,?,?)''', (Book_name, Author_name, Quantity))
    conn.commit()

    print("\nCurrent Stocks Present\n")
    
    cur.execute("SELECT Book_name, Author, Quantity FROM Main")
    myresult = cur.fetchall()


    print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock'], tablefmt='psql'))

def normal():

    import sqlite3
    from tabulate import tabulate

    conn = sqlite3.connect('Library.sqlite')
    cur=conn.cursor()

    Book_name=input("Enter Book name to be added to stock ")
    Author_name=input("Enter the author name ")
    Quantity=int(input("Enter the quantity "))

    cur.execute('''INSERT INTO Main (Book_name, Author, Quantity) VALUES (?,?,?)''', (Book_name, Author_name, Quantity))
    conn.commit()

    print("\nCurrent Stocks Present\n")

    cur.execute("SELECT Book_name, Author, Quantity FROM Main")
    myresult = cur.fetchall()


    print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock'], tablefmt='psql'))



