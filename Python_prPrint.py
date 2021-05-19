def print_stocks():
    import sqlite3
    from tabulate import tabulate
    conn=sqlite3.connect('library.sqlite')
    curr=conn.cursor()
    print("********** CURRENT STOCKS AVAILABLE *********")
    curr.execute("SELECT Book_name, Author, Quantity FROM Main")
    myresult = curr.fetchall()
    print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock'], tablefmt='psql'))

def print_student():
    import sqlite3
    from tabulate import tabulate
    conn=sqlite3.connect('library.sqlite')
    curr=conn.cursor()
    roll=int(input("Enter student roll no you want to find record "))
    curr.execute(''' SELECT Issue.Student_roll,Issue.Issue_id, Main.Book_Name, Issue.Issue_date from Main JOIN Issue on Main.Book_id=Issue.Book_id WHERE Student_roll=(?) ORDER BY Issue.Issue_id''',(roll,))
    table=curr.fetchall()
    print(tabulate(table,headers=[ 'Student Roll', 'Issue ID', 'Book Name','Issue Date'],tablefmt='psql'))

def issue_details():
    import sqlite3
    from tabulate import tabulate
    conn=sqlite3.connect('library.sqlite')
    curr=conn.cursor()
    curr.execute(''' SELECT Issue.Student_roll, Issue.Issue_id, Main.Book_name, Issue.Issue_date from Main JOIN Issue on Main.Book_id=Issue.Book_id ORDER BY Issue.Issue_date ''')
    table=curr.fetchall()
    print(tabulate(table,headers=[ 'Student Roll', 'Issue ID', 'Book Name','Issue Date'],tablefmt='psql'))


