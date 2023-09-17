import read_data as read
# import create_sql_light_db as create_db
# import delete_tables as delete
import compare_functions as compare
import extract_deviation as deviation
import display_graph_datasets as graphs
# import test_table_existence as test_table
# import unittest as test

# Read data from csv dataset and wride in to sqlite db tables
# create_db.create_tables_in_sqlight()


# test_table.table_exists('train')
# test_table.table_exists('ideal')
# test_table.table_exists('test')

# Read data from sqlite to 3 dataframes
df_train = read.read_data_to_train_df()
df_ideal = read.read_data_to_ideal_df()
df_test = read.read_data_to_test_df()

# Define 4 best fit ideal function similar to 4 train functions
df_4_best_fit_ideal = compare.define_optimal_from_ideal_to_train(df_train, df_ideal, df_test)
print('Print 4 best fit ideal functions with deviation:')
print(df_4_best_fit_ideal)

# Define number of one ideal best fit function similar to test function
best_fit_ideal = compare.get_best_function(df_4_best_fit_ideal)
print(f"Number of ideal function best fit to test function: {best_fit_ideal}")

# Define dediation between one ideal best fit function similar and test function
print(f"Display deviation for best fit function {best_fit_ideal}:")
result_df = deviation.define_deviation(df_ideal, df_test, best_fit_ideal)
print(result_df)

# Write result data in to table with best fit function and deviation
# create_db.write_data_in_db_table(result_df, 'result', best_fit_ideal)

#Display graphs
graphs.show_graph(df_train, df_test, df_ideal)

# Cleanup database
# delete.delete_tables()



