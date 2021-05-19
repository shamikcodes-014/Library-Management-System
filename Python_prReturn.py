def rbook():
  import sys
  import sqlite3
  from tabulate import tabulate
  import time
  conn=sqlite3.connect('library.sqlite')
  curr=conn.cursor()

  x=input("Enter Student Roll No.: ")
  time.sleep(3)

  print("Issue details of the student with roll no.", x, "is")


  curr.execute(''' SELECT Issue.Issue_id, Main.Book_Name, Main.Book_id, Issue.Student_roll, Issue.Issue_date from Main JOIN ISSUE on Main.Book_id=Issue.Book_id WHERE Student_roll=?''',(x,))  
  curr_lib=curr.fetchall()
  print(tabulate(curr_lib,headers=['Issue Id','Book Name','Book ID','Student Roll','Issue Date'],tablefmt='psql'))
    
  book_id_01=input("Enter the book id: ")
  issue_id=input("Enter the issue id: ")

  check=input("The condition of the book returned: ")

  if(check=='PERFECT CONDITION' or check=='Perfect Condition' or check=='Perfect' or check=='Not Damaged' or check=='NOT DAMAGED'):
    
    curr.execute('''UPDATE Main SET Quantity = Quantity + 1 WHERE Book_id= ?''',(book_id_01,))
    conn.commit()
    
    curr.execute('''DELETE FROM Issue WHERE Issue_id=?''',(issue_id,))
    conn.commit()
    print("The book has been returned succcessfully")
    
  elif(check=='DAMAGED' or check=='Damaged'):
    time.sleep(3)
    print("Book returned is in damaged condition, so a penalty of Rs.100 is imposed.")
    
    