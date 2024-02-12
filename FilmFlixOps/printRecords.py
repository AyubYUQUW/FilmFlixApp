from connect import *

# create a subroutine
def print_records():
    try:
        dbCursor.execute("SELECT * FROM tblFilms")
        
        #fetchall(): fetches all selected records
        row = dbCursor.fetchall()# row holds all fetched records
        
        #loop through all the records in the row variable
        for aRecord in row:
            #print all records
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")
if __name__ == "__main__":
    print_records()