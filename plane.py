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


def print_all_plane_from_heavy_bomber_class():
    """print all aircraft from Heavy Bomber class"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE plane_class = 'Heavy Bomber';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_plane_from_dive_bomber_class():
    """print all aircraft from Dive Bomber class"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE plane_class = 'Dive Bomber';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_plane_from_medium_bomber_class():
    """print all aircraft from Heavy Bomber class"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE plane_class = 'Medium Bomber';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()

def print_all_plane_from_ground_attack_class():
    """print all aircraft from Ground Attack class"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE plane_class = 'Ground Attack Aircraft';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_american():
    """print all aircraft from America"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin = 'United States';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_german():
    """print all aircraft from Germany"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin == 'Germany';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_british():
    """print all aircraft from United Kingdom"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin == 'United Kingdom';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_japanese():
    """print all aircraft from Japan"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin == 'Japan';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_soviet():
    """print all aircraft from the USSR"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin == 'USSR';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_italian():
    """print all aircraft from Italy"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin == 'Italy';"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"aircraft              top_speed    manufacturer             year_intro   country_origin     plane_class ")
    for plane in results:
        print(f'{plane[1]:<25}{plane[2]:<10}{plane[3]:<28}{plane[4]:<12}{plane[5]:<19}{plane[6]:<20}')
    #loop finishes here
    db.close()


def print_all_french():
    """print all aircraft from France"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM plane WHERE country_origin == 'France';"
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
5. Print all aircraft from Heavy Bomber class
6. Print all aircraft from Dive Bomber class
7. Print all aircraft from Medium Bomber class
8. Print all aircraft from Ground Attack aircraft class
9. Print all American aircraft 
10. Print all German aircraft 
11. Print all Japanese aircraft 
12. Print all British aircraft
13. Print all Soviet aircraft
14. Print all Italian aircraft 
15. Print all French aircraft
16. Exit
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
        print_all_plane_from_heavy_bomber_class() 
    if user_input == "6":
        print_all_plane_from_dive_bomber_class()
    if user_input == "7":
        print_all_plane_from_medium_bomber_class()
    if user_input == "8":
        print_all_plane_from_ground_attack_class()
    if user_input == '9':
        print_all_american()
    if user_input == '10':
        print_all_german()
    if user_input == "11":
        print_all_japanese()
    if user_input == '12':
        print_all_british()
    if user_input == "13":
        print_all_soviet()
    if user_input == "14":
        print_all_italian()
    if user_input == '15':
        print_all_french()
    if user_input == "16":
        break

    else:
        print("That is not an option")
