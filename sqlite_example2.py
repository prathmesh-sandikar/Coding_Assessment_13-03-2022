import sqlite3

def insertData(id, name, marks):
    con = sqlite3.connect('student.db')
    cursor = con.cursor()

    #paratrized query
    insert_query = '''INSERT INTO stud_marks
                         VALUES (?,?,?)'''

    cursor.execute(insert_query,(id, name, marks))

    con.commit()

    con.close()

a = int(input('enter the student id:'))
b = input('enter the student name:')
c = int(input('enter the student mark:'))
insertData(a,b,c)


