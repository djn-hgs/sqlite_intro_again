import sqlite3 as sql

with sql.connect('students.sqlite') as conn:
    cursor = conn.cursor()

    create_table_text = '''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT,
        age INTEGER,
        gender TEXT
        );
    '''

    cursor.execute(create_table_text)

    add_student = '''
    INSERT INTO student (firstname, lastname, age, gender)
    VALUES ('Kyrian', 'Salas', 17, 'Male');
    '''

    cursor.execute(add_student)

    add_student_with_placeholders = '''
    INSERT INTO student (firstname, lastname, age, gender)
    VALUES (?, ?, ?, ?);
    '''
    cursor.execute(add_student_with_placeholders, ('Gilad', 'Smith', 16, 'Male'))

    the_rest = [
        ('Michael', 'Tan-Sikorski', 16, 'Male'),
        ('Katya', 'Warner', 17, 'Female'),
        ('Luke', 'Willmott', 17, 'Male'),
        ('Daniel', 'Tunyan', 17, 'Male'),
    ]

    cursor.executemany(add_student_with_placeholders, the_rest)

