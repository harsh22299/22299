import sqlite3
#hello
DATABASE = 'SQL.db'

#open the database
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM Animals;"
cursor.execute(sql)
results = cursor.fetchall()

#print all the results
for animals in results:
#creates list
    print(f"animal_id: {animals[0]} animal_name: {animals[1]} scientific_name: {animals[2]} species_types: {animals[3]}")

#close the database
db.close()