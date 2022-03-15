# Write a Program for Customer Management:
#
#
#
#
# Create a ‘Customerdetails’ ⇒ id,name,city,tickets
#
#
# Options :
#
#
#        1.viewing the customer based on customer id
#
#        2. Total count of tickets sold
#
#        3. City wise ticket sold
#
#        4. Information ⇒ based on descending order
#
#        5. Update ⇒ customer id ⇒ which detail
#
#       6. Delete ⇒ customer id ⇒ delete the record


import sqlite3
con = sqlite3.connect('customer.db')

cursor = con.cursor()
# sqlite_query = '''CREATE TABLE customerdetails(
#                   cust_id INTEGER PRIMARY KEY,
#                   name TEXT NOT NULL,
#                   city TEXT NOT NULL,
#                   tickets INTEGER );'''
# cursor.execute(sqlite_query)
# print('table is created successfully')

def insertMultipleData(DataList):
    # paratrized query
    con = sqlite3.connect('customer.db')

    cursor = con.cursor()
    insert_query = '''INSERT INTO customerdetails
                         VALUES (?,?,?,?)'''

    cursor.executemany(insert_query, DataList)

    con.commit()
    print('total records inserted:', cursor.rowcount)
    con.commit()

    con.close()

def selectQry():
    con = sqlite3.connect('customer.db')
    Id = int(input('enter customer Id:'))

    cursor = con.cursor()
    sqlite_select_query = '''SELECT * FROM customerdetails
                            WHERE cust_id = ? '''

    cursor.execute(sqlite_select_query, (Id,))
    con.commit()

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('cust_id: ', row[0])
        print('name: ', row[1])
        print('city: ', row[2])
        print('tickets: ', row[3])

    con.close()



def OrderBy():
    con = sqlite3.connect('customer.db.db')

    cursor = con.cursor()
    sqlite_select_query = '''SELECT  name FROM customerdetails
                                ORDER BY name DESC'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    # for row in records:
    #     print('stud_id: ', row[0])
    #     print('name: ', row[1])
    #     print('marks: ', row[2])
    #     print('city: ', row[3])

    con.close()



    # connection = sqlite3.connect('customer.db')
    #
    # # sql query to display address and id
    # # based on address in descending order
    # cursor = connection.execute(
    #     "SELECT cust_id,name from customerdetails ORDER BY cust_id DESC")
    #
    # # display data row by row
    # for i in cursor:
    #     print(i)
    #
    # # close the connection
    # connection.close()






#DataList = [(7,'anny','pune',4),(6,'samuel','Bang',3),(4,'ronny','chennai',5)]
#insertMultipleData(DataList)

selectQry()
# OrderBy()

