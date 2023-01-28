import sqlite3


def creat_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as error:
        print(error)
    return conn

def add_product(conn, product):
    try:
        sql = '''INSERT INTO product 
        (product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_limit(conn, limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ?, quantity >= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def update_quantity_and_price(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ?, price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)


database = r'hw.db'
sql_create_product_table = '''

CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE (10 ,2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

connection = creat_connection(database)
if connection is not None:
    print('Connected successfully')
    # add_product(connection ,sql_create_product_table)
    # add_product(connection, ('Apple', 85, 5))
    # add_product(connection, ('Potatos', 55, 4))
    # add_product(connection, ('Tomat', 100, 1))
    # add_product(connection, ('Мыло', 208, 1))
    # add_product(connection, ('Жидкое мыло', 111, 2))
    # add_product(connection, ('Детское мыло', 100, 3))
    # add_product(connection, ('Масло', 99, 4))
    # add_product(connection, ('Сливочное масло', 88, 5))
    # add_product(connection, ('Подсолнечное масло', 57, 6))
    # add_product(connection, ('Сахар', 87, 7))
    # add_product(connection, ('Мука Казахстанское', 84, 8))
    # add_product(connection, ('Мука Кыргызстанское', 58, 9))
    # add_product(connection, ('Конфеты', 14, 1))
    # add_product(connection, ('Шоколад', 15, 2))
    # add_product(connection, ('Молочный шоколад', 16, 2))
    # select_all_products(connection)
    # select_limit(connection, 100)
    # update_quantity_and_price(connection, (56, 3, 2))
    # delete_product(connection, 2)
    # search_by_word(connection, 'мыло')
    connection.close()
    print('DONE')
