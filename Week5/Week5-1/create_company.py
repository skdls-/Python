import sqlite3

company = sqlite3.connect("company.db")
company.row_factory = sqlite3.Row
cursor = company.cursor()

cursor.execute('''DROP TABLE users''')
company.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users2(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
''')


cursor.execute('''INSERT INTO users2(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Ivo Ivanov",5000,  10000, "Software Developer"))

cursor.execute('''INSERT INTO users2(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Rado Rado",500 ,  0, "Tech Supp"))

cursor.execute('''INSERT INTO users2(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Ivo Ivo", 10000,  100000, "CEO"))

cursor.execute('''INSERT INTO users2(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Petar Petrov",3000,  1000, "Marketing Manager"))

cursor.execute('''INSERT INTO users2(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', ("Maria Georgieva", 8000,  10000, "COO"))

print ("first user updated")
company.commit()