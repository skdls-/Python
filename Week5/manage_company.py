import sqlite3


company = sqlite3.connect("company.db")
company.row_factory = sqlite3.Row
cursor = company.cursor()

def list_employees():
    result = cursor.execute('''SELECT name, position FROM users2''')
    for user in result:
        print('{} - {}'.format(user['name'], user['position']))
    company.commit()

def monthly_spending():

    result = cursor.execute('''SELECT SUM(monthly_salary) AS sum FROM users2''')
    total_monthly_salaries = cursor.fetchall()['sum']
    company.commit()
    return total_monthly_salaries

def yearly_spending():
    return monthly_spending() * 12
    company.commit()

def add_employee():
    employee = input("<name>, <monthly_salary>, <yearly_bonus>, <position>")
    employee = employee.split()
    name = employee[0]
    monthly_salary = employee[1]
    yearly_bonus = employee[2]
    position = employee[3]
    cursor.execute('''INSERT INTO users2(name, monthly_salary, yearly_bonus, position) 
                    VALUES(?,?,?,?)''', (name, monthly_salary,yearly_bonus, position))
    company.commit()


def delete_employee():
    emp_index = input("<id>")
    print(emp_index)
    cursor.execute('''DELETE FROM users2 WHERE id = ? ''', (emp_index,))
    company.commit()

def update_employee():
    emp_info  = input("<id>, <name>, <monthly_salary>, <yearly_bonus>, <position>")
    emp_info = emp_info.split()
    emp_index = emp_info[0]
    emp_name = emp_info[1]
    emp_month_salary = emp_info[2]
    emp_yearly_bonus = emp_info[3]
    emp_position = emp_info[4]
    cursor.execute('''UPDATE users2 SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?''' , (emp_name, emp_month_salary, emp_yearly_bonus, emp_position, emp_index))
    company.commit()