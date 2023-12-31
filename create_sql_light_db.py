import sqlite3
import pandas as pd


def create_tables_in_sqlight() -> None:
    """
    Funtion 1. create 3 tables in Sqlite database: test, train and ideal
    then 2. it reads data from 3 datasets and load it in Sqlite created tables
    """
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()

    # create tables
    c.execute('''CREATE TABLE test (x float, y float)''')
    c.execute('''CREATE TABLE train (x float, y1 float, y2 float, y3 float, y4 float)''')
    c.execute(
        '''CREATE TABLE ideal (x float, y1 float, y2 float, y3 float, y4 float, y5 float, y6 float, y7 float, y8 float, y9 float, y10 float, y11 float, y12 float, y13 float, y14 float, y15 float, y16 float, y17 float, y18 float, y19 float, y20 float, y21 float, y22 float, y23 float, y24 float, y25 float, y26 float, y27 float, y28 float, y29 float, y30 float, y31 float, y32 float, y33 float, y34 float, y35 float, y36 float, y37 float, y38 float, y39 float, y40 float, y41 float, y42 float, y43 float, y44 float, y45 float, y46 float, y47 float, y48 float, y49 float, y50 float)''')

    # load the data into a Pandas DataFrame
    try:
        # Attempt to read the CSV file
        test = pd.read_csv('data/test.csv')
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        # Handle the case where the file is empty
        print("The file is empty.")
    except pd.errors.ParserError:
        # Handle the case where there is an issue parsing the CSV data
        print("There was an issue parsing the CSV file.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")

    try:
        # Attempt to read the CSV file
        train = pd.read_csv('data/train.csv')
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        # Handle the case where the file is empty
        print("The file is empty.")
    except pd.errors.ParserError:
        # Handle the case where there is an issue parsing the CSV data
        print("There was an issue parsing the CSV file.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")

    try:
        # Attempt to read the CSV file
        ideal = pd.read_csv('data/ideal.csv')
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        # Handle the case where the file is empty
        print("The file is empty.")
    except pd.errors.ParserError:
        # Handle the case where there is an issue parsing the CSV data
        print("There was an issue parsing the CSV file.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")

    # write the data to a sqlite table
    test.to_sql('test', conn, if_exists='append', index=False)
    train.to_sql('train', conn, if_exists='append', index=False)
    ideal.to_sql('ideal', conn, if_exists='append', index=False)

    conn.close()


# create_tables_in_sqlight()

def write_data_in_db_table(df: pd.DataFrame, name: str, ideal_func_col: str) -> None:
    """
    Function create table rusult in Sqlite db and write in it data from dataframe passed as parameter
    :param df: Dataframe with data
    :param name: name of the table to be created
    :param ideal_func_col: column name of the ideal function, passed as parameter
    :return:
    """
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()
    create_table_sql = f"CREATE TABLE {name} (x float, y float, {ideal_func_col} float, deviation float)"
    c.execute(create_table_sql)
    df.to_sql(name, conn, if_exists='append', index=False)
    conn.close()
