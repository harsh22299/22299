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
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()



#main code 
while True:
    user_input = input("\nWhat would you like to do?.\n1.Print all aircraft\n2.Exit\n")
if user_input == "1":
    print_all_plane()
if user_input == "2":
    pass
else:
    print("That is not an option\n")
