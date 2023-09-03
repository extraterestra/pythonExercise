import unittest
import sqlite3
import create_sql_light_db as create_tables
import pandas as pd
import os


class TestDataLoading(unittest.TestCase):

    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the database connection after each test
        self.conn.close()

    def test_data_loading(self):
        # Call create_tables_in_sqlite function
        create_tables(self.conn)

        # Check if the data has been loaded into the tables correctly
        self.assertTrue(self.is_table_empty('test'))
        self.assertTrue(self.is_table_empty('train'))
        self.assertTrue(self.is_table_empty('ideal'))

    def is_table_empty(self, table_name):
        # Check if the specified table is empty
        query = f"SELECT COUNT(*) FROM {table_name}"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count == 0

if __name__ == '__main__':
    unittest.main()
