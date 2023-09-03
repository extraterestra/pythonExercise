import sqlite3

def delete_tables():
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()

    # delete tables
    c.execute('''DROP TABLE test''')
    c.execute('''DROP TABLE ideal''')
    c.execute('''DROP TABLE train''')
    c.execute('''DROP TABLE result''')

delete_tables()