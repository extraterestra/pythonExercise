import read_data as read
# import create_sql_light_db as create_db
# import delete_tables as delete
import compare_functions as compare
import extract_deviation as deviation
import display_graph_datasets as graphs

# create_db.create_tables_in_sqlight()

df_train = read.read_data_to_train_df()
df_ideal = read.read_data_to_ideal_df()
df_test = read.read_data_to_test_df()

compare.define_optimal_from_ideal_to_train()

deviation.define_deviation()

graphs.show_graph()

# delete.delete_tables()



