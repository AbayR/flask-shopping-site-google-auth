import sqlite3

# create empty database
connection = sqlite3.connect("database.db")
# communicate with the database
cursor = connection.cursor()



command1 = """
        CREATE TABLE IF NOT EXISTS shirts(id INTEGER PRIMARY KEY NOT NULL, samplename TEXT, image TEXT, price FLOAT, kind TEXT, typeClothes TEXT)
"""
cursor.execute(command1)

command2 = """
        CREATE TABLE IF NOT EXISTS cart(image TEXT, samplename TEXT, qty INTEGER, price FLOAT, subTotal FLOAT, id INTEGER PRIMARY KEY NOT NULL)
"""
cursor.execute(command2)

command3 = """
        CREATE TABLE IF NOT EXISTS purchases(uid INTEGER, samplename TEXT, image TEXT, quantity INTEGER, id INTEGER PRIMARY KEY NOT NULL, date DATE NOT NULL DEFAULT CURRENT_DATE,
        FOREIGN KEY(uid) REFERENCES users(id))
"""
cursor.execute(command3)

command4 = """
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY NOT NULL, username TEXT, password TEXT, email TEXT)
"""
cursor.execute(command4)


cursor.execute( "insert into shirts values (1, 'sample', 'sample0.jpg', 5100.0, 'casual', 'shirt')")
cursor.execute( "insert into shirts values (2, 'sample1', 'sample1.jpg', 5300.0, 'formal', 'shirt')")
cursor.execute("insert into shirts values (3, 'sample2', 'sample2.jpg', 7900.0, 'formal', 'shirt')")
cursor.execute("insert into shirts values (4, 'sampleshoe1', 'sampleshoe1.jpg', 8900.0, 'casual', 'shoe')")
cursor.execute("insert into shirts values (5, 'sampleshoe2', 'sampleshoe2.jpg', 9900.0, 'formal', 'shoe')")
cursor.execute("insert into shirts values (6, 'samplepant1', 'samplepant1.jpg', 5500.0, 'casual', 'pant')")
cursor.execute("insert into shirts values (7, 'samplepant2', 'samplepant2.jpg', 7500.0, 'casual', 'pant')")

connection.commit()


connection.close()