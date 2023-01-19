import sqlite3 as sql

with sql.connect('students.sqlite') as conn:
    cursor = conn.cursor()

    select_query = '''
    SELECT firstname, lastname FROM student
    WHERE age = 17
    '''

    cursor.execute(select_query)
    student = cursor.fetchall()

    print(student)
