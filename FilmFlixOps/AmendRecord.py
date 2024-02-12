from connect import * 

# create a subroutine
def update_records():
 
    
    try:
        #  the id of the record to be updated 
        idField = input("Enter the filmID to update a record: ")

        # select a record using filmID from the table
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField} ")

        row = dbCursor.fetchone() # use the fetchone() to fetch the selected record
        #None: A singleton object used to check/signal if value is absent
        if row == None: # row is the record returned based on the specific filmID
            print(f"No record wih the filmID {idField} exists")
        
        else:
            # the field selected for update 
            fieldName = input("Enter the field (Title or YearReleased or Rating or Duration or Genre) to update: ").title()

            # the value to be entered in the field 
            fieldValue = input(f"Enter the value for the {fieldName}: ")

            # add quotes to field value 
            fieldValue = "'"+fieldValue+"'"

             
            #use filmID is a primary and a unique field to update a record
            dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField} ")
            dbCon.commit()
            print(f"{idField} Updated in the records table ")
    except sql.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_records()
