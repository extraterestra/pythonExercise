import sqlite3

conn = sqlite3.connect('my_data.db')
c = conn.cursor()

# delete tables
c.execute('''DROP TABLE test''')
c.execute('''DROP TABLE ideal''')
c.execute('''DROP TABLE train''')
c.execute('''DROP TABLE result''')
