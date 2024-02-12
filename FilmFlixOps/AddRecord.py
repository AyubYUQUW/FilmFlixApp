from connect import *

# create a subroutine
def insert_records():
 # create an empty list
 records = []
 # ask for user input (MemberID, Firstname, Lastname and Email)
 # MemberID is an auto increment field and does not require input

 Title = input("Enter Title: ")
 yearReleased = input("Enter Year Released: ")
 rating = input("Enter rating: ")
 Duration = input("Enter duration: ")
 Genre = input("Enter Genre: ")
 
 print(f"Data: {Title, yearReleased, rating, Duration, Genre}")

 # append data Firstname, Lastname and Email

 records.append(Title)
 records.append(yearReleased)
 records.append(rating)
 records.append(Duration)
 records.append(Genre)
 print(f"The members list {records}")

 #"INSERT INTO members VALUES(NULL, 'A','B','C')"
 #"INSERT INTO members (Firstname, Lastname , Email) VALUES( 'A','B','C')"

 try:
    dbCursor.execute("INSERT INTO tblFilms VALUES(NULL, ?,?,?,?,?)", records) # Values from the list
   # or
   # values directly from variables
   # dbCursor.execute("INSERT INTO members VALUES(NULL, ?,?,?)", (fName,lName,email))
   # dbCursor.execute("INSERT INTO members (Firstname, Lastname , Email) VALUES( '?','?','?')")
    dbCon.commit() # make the changes permanent
    print(f"{Title} inserted in the Table")
 except sql.OperationalError as e:
  dbCon.rollback()
  print(f"Insert failed {e}")
if __name__== "__main__":
  insert_records()