import sqlite3

con = sqlite3.connect('python.db')
cur = con.cursor()

sql = '''CREATE TABLE pyversions (
   branch CHAR PRIMARY KEY,
   released_at_year INTEGER,
   released_at_month INTEGER,
   release_manager CHAR
)'''

cur.execute(sql)
branch = 3.9
released_at_year = 2020
released_at_month = 10
release_manager = 'Łukasz Langa'

sql = f'INSERT INTO pyversions VALUES ({branch}, {released_at_year}, {released_at_month}, "{release_manager}")'

cur.execute(sql)