import sqlite3
import Python_prAdd
import Python_prDelete
import Python_prEdit
import Python_prIssue
import Python_prReturn
import Python_prPrint

print(" 1. Add Sock\n 2. Delete Stock\n 3. Issue Book\n 4. Return Book\n 5. Edit Stocks\n 6.Print")
inp=input("Enter your choice ")
if inp=="1":
    inp2=input("Are you creating the database for the first time ")
    if inp2=="Yes" or inp2=="YES" or inp2=="YEs" or inp2=="yes" or inp2=="yES":
        Python_prAdd.first()
    else:
        
        Python_prAdd.normal()
        
if inp=="2":
    inp3=input(" 1.Delete a book record\n 2.Delete entire database\n")
    if inp3=="1":
        Python_prDelete.delete()
    elif inp3=="2":
        Python_prDelete.delete_data()
    else:
        print(" WRONG CHOICE, ENTER AGAIN ")
if inp=="3":
    inp4=input(" 1.Create New Issue Database\n 2.Add new Issue Record\n")
    if inp4=="1":
        Python_prIssue.issue_new()
    elif inp4=="2":
        Python_prIssue.issue_existing()
    else:
        print(" WRONG CHOICE, ENTER AGAIN")
if inp=="4":
    Python_prReturn.rbook()

if inp=="5":
    Python_prEdit.edit()
if inp=="6":
    inp5=input(" 1.Print Current Stock Records\n 2.Print current issue table records.\n 3.Print particular student records\n ")
    if inp5=="1":
        Python_prPrint.print_stocks()
    elif inp5=="2":
        Python_prPrint.issue_details()
    elif inp5=="3":
        Python_prPrint.print_student()
    else:
        print(" WRONG CHOICE, ENTER AGAIN")
