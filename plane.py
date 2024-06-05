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


def print_all_plane_sorted_speed():
    '''print all the plane sorted by speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT *  FROM plane ORDER BY top_speed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_plane_sorted_year_intro():
    """print all aircraft sorted by year introduced"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane ORDER BY year_intro DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_plane_from_fighter_class():
    """print all aircraft from fighter class"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE plane_class = 'Fighter';"
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
    user_input = input(
"""
What would you like to do?
1. Print all aircraft.
2. Print all aircraft sorted by speed.
3. Print all aircraft sorted by year introduced
4. Print all aircraft from Fighter class
5. Exit
""")
    if user_input == "1":
        print_all_plane()
    if user_input == "2":
        print_all_plane_sorted_speed()
    if user_input == "3":
        print_all_plane_sorted_year_intro()
    if user_input == "4":
        print_all_plane_from_fighter_class()
    if user_input == "5":
        break 
    else:
        print("That is not an option\n")
