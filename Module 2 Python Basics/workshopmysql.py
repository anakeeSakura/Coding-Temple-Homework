import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ssirisavath',
    database='students_db'
)

cursor = connection.cursor()

if connection.is_connected():
    print('Successfully connected to database!')
cursor.execute('Create Database If Not Exists demo_db')

cursor.execute('Show Databases')
for db in cursor:
    print(db)

# create a database
cursor.execute('Create Database demo_db')

#verify database was created
cursor.execute('Show Databases')
for db in cursor:
    print(db)


#Creating a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        NAME VARCHAR(50) 
    ''')

#verify table was created
cursor.execute('Show Tables')
for table in cursor:
    print(table)

#DML: Data Manupulation Language
query = '''
    INSERT INTO instructors(
        name
    ) Values (
        'Sakura'
    )
        
        '''
#perform the query
cursor.execute(query)

#commit/save changes to database
connection.commit()

#DQL: Data query Language
cursor.execute('''
SELECT *
From instructors'''
)

# commit/save changes to database
connection.commit()

# Delete Data in a table: Delete an instructor
query = '''
    DELETE FROM instructors
    WHERE id = 2 
'''
cursor.execute(query)

# fetch all rows
rows = cursor.fetchall()

#Update data in a table; Update an instructors name
cursor.execute('''
    UPDATE instructors
    SET name = 'Christian'
    WHERE id = 9 
''')

#always remember to close cursor and connection at the bottom of script
cursor.close()
connection.close()
