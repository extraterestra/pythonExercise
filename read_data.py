import sqlite3
import pandas as pd

def connect_to_db():
    conn = sqlite3.connect('my_data.db')
    conn.cursor()
    return conn
def read_data_to_test_df():
    conn = connect_to_db()
    test_df = pd.read_sql('''SELECT * FROM test''', conn)
    return test_df

def read_data_to_train_df():
    conn = connect_to_db()
    train_df = pd.read_sql('''SELECT * FROM train''', conn)
    return train_df

def read_data_to_ideal_df():
    conn = connect_to_db()
    ideal_df = pd.read_sql('''SELECT * FROM ideal''', conn)
    return ideal_df
