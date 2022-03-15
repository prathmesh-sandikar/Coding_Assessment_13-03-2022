
# Create a menu-driven Python project “ Employee Management System” to manage the
# employees in a company using sqlite database.




import sqlite3

con = sqlite3.connect('employee_management.db')

cursor = con.cursor()


sqlite_query = '''CREATE TABLE Employee(
                  empCode INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  phone TEXT NOT NULL,
                  email TEXT NOT NULL,
                  designation TEXT NOT NULL,
                  salary REAL NOT NULL,
                  company_name TEXT NOT NULL);'''
cursor.execute(sqlite_query)
print('table is created successfully')


# 1. Add the Employees ( empCode, name, phone, email, designation, salary, company
# name )

def Add_An_Employee():
    Emp_Code = input("Enter Employee Code : ")
    Name = input("Enter Employee Name : ")
    Phone_no = input("Enter Employee's phone no. : ")
    Email = input("Enter Employee's email : ")
    Designation = input("Enter Designation : ")
    Salary = input("Enter Employee Salary : ")
    Company = input("Enter Company Name : ")
    data = (Emp_Code, Name, Phone_no, Email, Designation, Salary, Company)

    insert_query = '''INSERT INTO Employee
                                 VALUES (?,?,?,?,?,?,?)'''

    cursor.execute(insert_query, data)

    con.commit()

    print("Employee Added Successfully\n ")
    menu()


# 2. View All employees
def Display_Employees():
    sqlite_select_query = '''SELECT * FROM Employee'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])
        print("---------------------")

    menu()

# 3. Search an employee using employee name
def Search_An_Employee():
    Name = input("enter Employee Name : ")

    sqlite_select_query = '''SELECT * FROM Employee
                                WHERE name = ?'''

    cursor.execute(sqlite_select_query, (Name,))

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])

    menu()


# 4. Update an employee details using employee Code
def Update_An_Employees():
    Emp_Code = input("Enter Employee Code : ")
    Name = input("Enter Employee Name : ")
    Phone_no = input("Enter Employee'sphone no. : ")
    Email = input("Enter Employee's email : ")
    Designation = input("Enter Designation : ")
    Salary = input("Enter Employee Salary : ")
    Company = input("Enter Company Name : ")

    updt_query = '''UPDATE Employee
                        SET name = ?,phone = ?, email = ?,designation = ?, salary = ?, company_name = ?
                        WHERE empCode = ?'''
    data = (Name, Phone_no, Email, Designation, Salary, Company, Emp_Code)
    cursor.execute(updt_query, data)
    con.commit()
    print("Total", cursor.rowcount, "Records updated successfully")
    con.commit()
    #con.close()
    menu()


# 5. Delete an employee using employee Code
def Delete_Employee():
    Emp_Code = input("Enter Employee Code : ")
    sqlite_delete_query = '''DELETE FROM Employee
                                WHERE empCode = ?'''

    cursor.execute(sqlite_delete_query, (Emp_Code,))

    con.commit()
    print("Employee Deleted")

    menu()


# 6. Display all the details of employees whose salary is greater than 50000
def Display_Employees():
    sqlite_select_query = '''SELECT * FROM Employee
                                WHERE salary > 50000'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])

    menu()


# 7. Display the count of total number of employees in the company
def Count_Employee():
    sqlite_count_query = '''SELECT COUNT(name) FROM Employee'''

    cursor.execute(sqlite_count_query)

    count_employee = cursor.fetchone()
    print('total no of employees : ', count_employee[0])

    menu()


# 8. Display all the employee details in alphabetical order, within the specific salary range
# (lower salary amount and higher amount range should be read from the user. Eg: lower
# salary range 25000 & higher salary range 60000).

def salary_range():
    min_salary = input('Enter min salary range: ')
    max_salary = input('Enter max salary range: ')

    sqlite_select_query = '''SELECT * FROM Employee
                                    WHERE salary BETWEEN ? AND ?
                                    ORDER BY name ASC'''

    data = (min_salary, max_salary)
    cursor.execute(sqlite_select_query, data)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])



    menu()


# 9. Display all the employees data, whose salary is less than the average salary of all the
# employees '''
def Display_Avg_Employees():
    sqlite_select_query = '''SELECT * FROM Employee
                                    WHERE salary < (SELECT avg(salary)FROM Employee)'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])


    menu()

def menu():
    print("\n\nPress ")
    print("1 for Add Employee")
    print("2 for View All employees ")
    print("3 for Search an employee using employee name")
    print("4 for Update an employee details using employee Code")
    print("5 for Delete an employee using employee Code")
    print("6 for Display all the details of employees whose salary is greater than 50000")
    print("7 for Display the count of total number of employees in the company")
    print("8 for Display all the employee details in alphabetical order, within the specific salary range")
    print("9 for Display the employees data, whose salary is less than the average salary of all the employees")
    print("10 for Exit")

    ch = int(input("Enter your Choice :"))
    if ch == 1:
        Add_An_Employee()
    elif ch == 2:
        Display_Employees()
    elif ch == 3:
        Search_An_Employee()
    elif ch == 4:
        Update_An_Employees()
    elif ch == 5:
        Delete_Employee()
    elif ch == 6:
        Display_Employees()
    elif ch == 7:
        Count_Employee()
    elif ch == 8:
        salary_range()
    elif ch == 9:
        Display_Avg_Employees()
    elif ch == 10:
        exit(0)
    else:
        print("Invalid Choice")
        menu()


menu()



