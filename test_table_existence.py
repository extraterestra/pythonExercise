import unittest
import sqlite3


# Function to check if a table exists in the database
def table_exists(table_name):
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()

    # Try to execute a SELECT query on the specified table
    try:
        c.execute(f"SELECT * FROM {table_name} LIMIT 1")
        conn.close()
        return True
    except sqlite3.OperationalError:
        conn.close()
        return False


class TestTableExistence(unittest.TestCase):
    def test_result_table_exists(self):
        # Replace 'table_name_to_check' with the actual table name you want to check
        table_name_to_check = 'result'

        # Check if the table exists
        self.assertTrue(table_exists(table_name_to_check))

    def test_test_table_exists(self):
        # Replace 'table_name_to_check' with the actual table name you want to check
        table_name_to_check = 'test'

        # Check if the table exists
        self.assertTrue(table_exists(table_name_to_check))

    def test_ideal_table_exists(self):
        # Replace 'table_name_to_check' with the actual table name you want to check
        table_name_to_check = 'ideal'

        # Check if the table exists
        self.assertTrue(table_exists(table_name_to_check))

    def test_train_table_exists(self):
        # Replace 'table_name_to_check' with the actual table name you want to check
        table_name_to_check = 'train'

        # Check if the table exists
        self.assertTrue(table_exists(table_name_to_check))


if __name__ == '__main__':
    unittest.main()
