import sqlite3
import pandas as pd

def create_tables_in_sqlight():
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()

    # Clean up
    # c.execute('''DROP TABLE test''')
    # c.execute('''DROP TABLE ideal''')
    # c.execute('''DROP TABLE train''')
    # c.execute('''DROP TABLE result''')

    # create tables
    c.execute('''CREATE TABLE test (x float, y float)''')
    c.execute('''CREATE TABLE train (x float, y1 float, y2 float, y3 float, y4 float)''')
    c.execute('''CREATE TABLE ideal (x float, y1 float, y2 float, y3 float, y4 float, y5 float, y6 float, y7 float, y8 float, y9 float, y10 float, y11 float, y12 float, y13 float, y14 float, y15 float, y16 float, y17 float, y18 float, y19 float, y20 float, y21 float, y22 float, y23 float, y24 float, y25 float, y26 float, y27 float, y28 float, y29 float, y30 float, y31 float, y32 float, y33 float, y34 float, y35 float, y36 float, y37 float, y38 float, y39 float, y40 float, y41 float, y42 float, y43 float, y44 float, y45 float, y46 float, y47 float, y48 float, y49 float, y50 float)''')
    c.execute('''CREATE TABLE result (x float, y float, ideal_func float, deviation float)''')

    # load the data into a Pandas DataFrame
    test = pd.read_csv('data/test.csv')
    train = pd.read_csv('data/train.csv')
    ideal = pd.read_csv('data/ideal.csv')

    # write the data to a sqlite table
    test.to_sql('test', conn, if_exists='append', index = False)
    train.to_sql('train', conn, if_exists='append', index = False)
    ideal.to_sql('ideal', conn, if_exists='append', index = False)


create_tables_in_sqlight()

