def issue_new():
    import sqlite3
    from tabulate import tabulate
    import datetime
    conn=sqlite3.connect('library.sqlite')
    cur=conn.cursor()
    cur.executescript('''
     DROP TABLE IF EXISTS Issue;

    CREATE TABLE Issue (
        Issue_id VARCHAR(128) NOT NULL PRIMARY KEY UNIQUE,
        Book_id INTEGER NOT NULL,
        Student_roll INTEGER NOT NULL,
        Issue_date TEXT NOT NULL        
        )    
    ''')

    Roll=int(input("Enter Student roll no. : "))

    print("\nCurrent Stocks Present\n")
    
    cur.execute("SELECT Book_name, Author, Quantity, Book_id FROM Main")
    myresult = cur.fetchall()
    print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock', 'Book ID'], tablefmt='psql'))

    book_id=input("Enter book id(s) of the books student wants to be borrow : ").split(",")
    x = tuple(book_id)
    for i in x:
            query="INSERT INTO Issue (Issue_id, Book_id, Student_roll, Issue_date) VALUES (?,?,?,?)"
            cur.execute('''SELECT Book_name FROM Main WHERE Book_id = ?''',(i,))
            n=cur.fetchone()[0]
            I_id=n+str(Roll)
            data=(I_id,i,Roll,datetime.datetime.now())
            cur.execute(query,data)
            cur.execute('UPDATE Main SET Quantity = Quantity - 1 WHERE Book_id = ?',(i,))
            conn.commit()
    
    print("\n********PRINTING ISSUE TABLE********\n")
    
    cur.execute("SELECT Issue_id, Book_id, Student_roll, Issue_date FROM Issue")
    myresult = cur.fetchall()
    print(tabulate(myresult, headers=['Issue ID', 'Book ID', 'Student Roll No.', 'Issue Date'], tablefmt='psql'))
    
def issue_existing():

    import sqlite3
    from tabulate import tabulate
    import datetime
    conn=sqlite3.connect('library.sqlite')
    cur=conn.cursor()
    
    Roll=int(input("Enter Student roll no. : "))

    print("\nCurrent Stocks Present\n")
    
    cur.execute("SELECT Book_name, Author, Quantity, Book_id FROM Main")
    myresult = cur.fetchall()
    print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock', 'Book ID'], tablefmt='psql'))

    book_id=input("Enter book id(s) of the books student wants to be borrow : ").split(",")
    x = tuple(book_id)
    for i in x:
            query="INSERT INTO Issue (Issue_id, Book_id, Student_roll, Issue_date) VALUES (?,?,?,?)"
            cur.execute('''SELECT Book_name FROM Main WHERE Book_id = ?''',(i,))
            n=cur.fetchone()[0]
            I_id=n+str(Roll)
            data=(I_id,i,Roll,datetime.datetime.now())
            cur.execute(query,data)
            cur.execute('UPDATE Main SET Quantity = Quantity - 1 WHERE Book_id = ?',(i,))
            conn.commit()
    
    print("\n********PRINTING ISSUE TABLE********\n")
    
    cur.execute("SELECT Issue_id, Book_id, Student_roll, Issue_date FROM Issue")
    myresult = cur.fetchall()
    print(tabulate(myresult, headers=['Issue ID', 'Book ID', 'Student Roll No.', 'Issue Date'], tablefmt='psql'))









    



    