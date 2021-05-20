def delete():
  import sqlite3
  from tabulate import tabulate
  conn=sqlite3.connect('library.sqlite')
  curr=conn.cursor()


  print("\n\n********** CURRENT LIBRARY STOCKS ***********\n\n")
  curr.execute("SELECT Book_name, Author, Quantity, Book_id FROM Main")
  myresult = curr.fetchall()

  print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock', 'Book ID'], tablefmt='psql'))

  x=input("Enter the Book id to delete :")
  curr.execute('''DELETE FROM Main WHERE Book_id=?''',(x))
  conn.commit()

  print("\n\n********** UPDATED LIBRARY STOCKS ***********\n\n")
  curr.execute("SELECT Book_name, Author, Quantity, Book_id FROM Main")
  myresult = curr.fetchall()

  print(tabulate(myresult, headers=['Book Name', 'Author', 'In Stock', 'Book_id'], tablefmt='psql'))

def delete_data():

  import sqlite3
  from tabulate import tabulate
  conn=sqlite3.connect('library.sqlite')
  curr=conn.cursor()

  curr.execute(''' DROP TABLE IF EXISTS Main ''')
  print("\n\n********** LIBRARY DATABASE DELETED SUCCESSFULLY ***********\n\n")


