
def edit():
    
    import sqlite3
    from tabulate import tabulate
    
    con=sqlite3.connect('Library.sqlite')
    cur=con.cursor()
    
    print("\n\n********** PRINTING THE CURRENT LIBRARY DATABASE ***********\n\n")
    
    cur.execute(" SELECT Book_Name, Author, Quantity, Book_id FROM Main ")
    curr_lib=cur.fetchall()  
    print(tabulate(curr_lib,headers=['Book Name', 'Author', 'In Stock', 'Book ID'],tablefmt='psql'))
    
    BID=int(input("Enter the Book ID for which the details are to be altered: "))
    
    querySelect = "SELECT * FROM Main"
    queryWhere = " WHERE Book_id = " + str(BID)
    query = querySelect + queryWhere
    cur.execute(query)
    
    curr_lib=cur.fetchall()
    print("\n")
    print(tabulate(curr_lib,headers=['Book Name', 'Author', 'In Stock', 'Book ID'],tablefmt='psql'))
    print("\n")
    
    print("Enter which field you would like to Edit: \n")
    print("1. Book Name")
    print("2. Author")
    print("3. Stock")

    ch=int(input("\nEnter your choice from above options: ")) 
    
    if(ch==1):
        Bname=input("Enter the new Name of the Book: ")
        sql_update_query = """UPDATE Main SET Book_Name = ? where Book_id = ?"""
        data=(Bname,BID)

    if(ch==2):
        Bauth=input("Enter the new authour of the book: ")
        sql_update_query = """UPDATE Main SET Author = ? where Book_id = ?"""
        data = (Bauth, BID)
        
    if(ch==3):
        Bquant=int(input("Enter the new quantity of the Book: "))
        sql_update_query = """UPDATE Main SET Quantity = ? where Book_id = ?"""
        data=(Bquant,BID)
   
    cur.execute(sql_update_query, data)
    con.commit()
    print("\n Record Updated successfully")
    
    print("\n\n********* PRINTING THE UPDATED LIBRARY **********\n\n")
    
    cur.execute(" SELECT Book_name, Quantity, Author, Book_id FROM Main ")
    curr_lib=cur.fetchall()  
    print(tabulate(curr_lib,headers=['Book Name','In Stock','Author','Book ID'],tablefmt='psql'))
    
    

    
    
    