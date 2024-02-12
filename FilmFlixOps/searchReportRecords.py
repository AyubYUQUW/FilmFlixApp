from connect import *
import logging
import time
 
logging.basicConfig(filename=r" FilmFlixOps\file2.log",  level=logging.DEBUG)
filename = __file__
# create a subroutine
def search():
    try:
        field = input("Would you like to search by filmID or Title or YearReleased or Rating or Duration or Genre? ")
        if field == "filmID":
            idInput = input("Enter filmID: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idInput}:")
            row = dbCursor.fetchone()
            if row == None:
                print(f"No record with {idInput} exists in the table: ")
                logging.warning(f"on {time.asctime()}, file is {filename}, user entered {idInput} as {field}")
            else:
                for aRecord in row:
                    print(aRecord)
        elif field == "Title" or field == "YearReleased" or field == "Rating" or field == "Duration" or field == "Genre":
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{searchInput}%'")
            rows = dbCursor.fetchall()
            if rows == None:
                print(f"No record with field {field} Matching '{searchInput}' in the table ")
            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search filed {field}")
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
if __name__ == "__main__":
    search()