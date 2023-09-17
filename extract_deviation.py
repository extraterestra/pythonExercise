import pandas as pd

def define_deviation(df_ideal, df_test, num_ideal):
    # Sort the df_test by the 'x' column
    sorted_test_df = df_test.sort_values(by='x')

    # Drop the unnecessary columns except x and num_y_ideal as it's no longer needed
    df_ideal = df_ideal[['x', num_ideal]]

    # Merge the 'ideal' and 'test' DataFrames based on the common 'x' values
    df_result = pd.merge(sorted_test_df, df_ideal, on='x')

    # Calculate deviation as new column 'deviation'= y-num_y_ideal
    df_result['deviation'] = df_result['y'] - df_result[num_ideal]
    return df_result

def define_sum_deviation_for_function(function_y_id, df_test, df_ideal):
    sorted_test_df = df_test.sort_values(by='x')

    #Merge the 'ideal' and 'test' DataFrames based on the common 'x' values
    df_result = pd.merge(sorted_test_df, df_ideal, on='x')

    #Calculate total deviation for given function
    df_result['deviation'] = df_result['y'] - df_result[function_y_id]
    return df_result['deviation'].sum()

