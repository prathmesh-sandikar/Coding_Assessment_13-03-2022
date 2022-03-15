# Create a table students table having columns such as studentid,name,marks,city. Add 10 records and complete all the above task.
# Updating a record, Deleting a record,Group by based on city column, Count of Students, Average of Marks, Order them in descending order based on Marks

import sqlite3
con = sqlite3.connect('student_ex.db')

cursor = con.cursor()
# sqlite_query = '''CREATE TABLE students(
#                   stud_id INTEGER PRIMARY KEY,
#                   name TEXT NOT NULL,
#                   marks INTEGER NOT NULL,
#                   city TEXT NOT NULL);'''
# cursor.execute(sqlite_query)
# print('table is created successfully')


def insertMultipleData(DataList):
    # paratrized query
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    insert_query = '''INSERT INTO students
                         VALUES (?,?,?,?)'''

    cursor.executemany(insert_query, DataList)

    con.commit()
    print('total records inserted:', cursor.rowcount)
    con.commit()

    con.close()


def selectQry():
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    sqlite_select_query = '''SELECT * FROM students'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('stud_id: ', row[0])
        print('name: ', row[1])
        print('marks: ', row[2])
        print('city: ', row[3])

    con.close()


def update_qry(id, name, marks, city):
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    updt_query = '''UPDATE students
                        SET name = ?,marks = ?, city = ?
                        WHERE stud_id = ?'''
    data = (name, marks, city, id)
    cursor.execute(updt_query, data)
    con.commit()
    print("Total", cursor.rowcount, "Records updated successfully")
    con.commit()
    con.close()


def del_qry(idList):
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()

    del_query = '''DELETE FROM students
                           WHERE stud_id = ?'''

    cursor.executemany(del_query, idList)

    con.commit()

    print("Total", cursor.rowcount, "Records deleted successfully")

    con.close()



def OrderBy():
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    sqlite_select_query = '''SELECT * FROM students
                                ORDER BY marks'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    # for row in records:
    #     print('stud_id: ', row[0])
    #     print('name: ', row[1])
    #     print('marks: ', row[2])
    #     print('city: ', row[3])

    con.close()



def cnt_students():
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    sqlite_select_query = '''SELECT COUNT(stud_id) FROM students'''

    cursor.execute(sqlite_select_query)
    count_stud = cursor.fetchone()
    print(count_stud)



def avg_marks():
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    sqlite_select_query = '''SELECT AVG(marks) FROM students'''

    cursor.execute(sqlite_select_query)
    count_stud = cursor.fetchone()
    print('avg marks: ', count_stud)







def GroupBy():
    con = sqlite3.connect('student_ex.db')

    cursor = con.cursor()
    sqlite_select_query = '''SELECT COUNT(stud_id), city FROM students
                                GROUP BY city'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    # for row in records:
    #     print('stud_id: ', row[0])
    #     print('name: ', row[1])
    #     print('marks: ', row[2])
    #     print('city: ', row[3])

    con.close()


#DataList = [(2,'anny',97,'Dhule'),(3,'samuel',95,'Malegaon'),(4,'Tomy',66,'Pune'),(5,'gaju', 97,'kolkata'),(6,'shubh',74,'Delhi'),(7,'kartik', 78,'Benglore'),(8,'govind',84,'Sangli'),(9,'Ashu',63,'Yavatmal'),(10,'raju', 69, 'Lonavala'),(11, 'shruti', 99, 'Ratnagiri')]
#insertMultipleData(DataList)
#update_qry(2, 'sandy', 65, 'Delhi')
#idsToDelete = [(2,)]
#del_qry(idsToDelete)
selectQry()
#OrderBy()
#cnt_students()
#avg_marks()
GroupBy()


