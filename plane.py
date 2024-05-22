#docstring- Harsh Gautam- ww2 plane database application
#imports
import sqlite3


DATABASE = "plane.db"


#functions
def print_all_plane():
    '''print all the plane neatly'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from plane;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    for plane in results:
        print(f'{plane[1]}{plane[2]}{plane[3]}{plane[4]}{plane[5]}{plane[6]}')
    #loop finishes here
    db.close()



#main code 
print_all_plane()