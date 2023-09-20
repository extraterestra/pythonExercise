import pandas as pd


def define_deviation(df_ideal: pd.DataFrame, df_test: pd.DataFrame, num_ideal: str) -> pd.DataFrame:
    """
    Function return dataframe with additional column Deviation
    calculated as difference of values y (y-num_y_ideal)
    from test and chosen ideal functions
    :param df_ideal: Dataframe with 50 ideal functions as x and y1,y2,...
    :param df_test: Dataframe with one test function as x and y
    :param num_ideal: Nume of best shosen ideal function
    :return: Dataframe with calculated results
    """
    # Sort the df_test by the 'x' column
    sorted_test_df = df_test.sort_values(by='x')

    # Drop the unnecessary columns except x and num_y_ideal as it's no longer needed
    df_ideal = df_ideal[['x', num_ideal]]

    # Merge the 'ideal' and 'test' DataFrames based on the common 'x' values
    df_result = pd.merge(sorted_test_df, df_ideal, on='x')

    # Calculate deviation as new column 'deviation'= y-num_y_ideal
    df_result['deviation'] = df_result['y'] - df_result[num_ideal]
    return df_result


def define_sum_deviation_for_function(function_y_id: str, df_test: pd.DataFrame,
                                      df_ideal: pd.DataFrame) -> pd.DataFrame:
    """
    Function calculate total deviation for given function
    :param function_y_id: name of chosen function
    :param df_test: Dataframe with data of one test function
    :param df_ideal: Dataframe with data of 50 ideal functions
    :return: Dataframe  with total deviation for each function
    """
    sorted_test_df = df_test.sort_values(by='x')

    # Merge the 'ideal' and 'test' DataFrames based on the common 'x' values
    df_result = pd.merge(sorted_test_df, df_ideal, on='x')

    # Calculate total deviation for given function
    df_result['deviation'] = df_result['y'] - df_result[function_y_id]
    return df_result['deviation'].sum()
