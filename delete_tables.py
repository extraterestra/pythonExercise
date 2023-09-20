import sqlite3


def delete_tables() -> None:
    """
    Function delete 4 tables: test, ideal, train, result
    """
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()

    # delete tables
    c.execute('''DROP TABLE test''')
    c.execute('''DROP TABLE ideal''')
    c.execute('''DROP TABLE train''')
    c.execute('''DROP TABLE result''')

    conn.close()

# delete_tables()
