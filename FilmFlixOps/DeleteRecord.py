from connect import *
 
# create a subroutine
def delete_records():
 
    try:
        #use filmID: is a primary and a unique field to delete a record
       # the id of the record to be deleted
        idField = input("Enter the filmID to delete a record: ")
 
        # select a record using filmID from the table
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField} ")
 
        row = dbCursor.fetchone() # use the fetchone() to fetch the selected record
        #None: A singleton object used to check/signal if value is absent
 
        if row == None:
            print(f"No record wih the filmID {idField} exists")
       
        else:
            dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField} ")
            dbCon.commit()
            print(f"Record {idField} deleted")
   
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
   
if __name__ == "__main__":
    delete_records()