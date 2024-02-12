import sqlite3 as sql # import the stardard sqlite3 module

try:
#To use the module, start by creating db connection object(variable to hold the folder/file)
# using the connect function from the sqlite3 module
 with sql.connect("FilmFlixOps/filmflix.db") as dbCon:
# once the connection and/or dbfile is created
# create a cursor object(variable) and call it cursor method
   dbCursor = dbCon.cursor() # use to execute sql statements

except sql.OperationalError as e: # raise sqlerror
# handle the exception/error raised
 print(f"Connection failed: {e}")