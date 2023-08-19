import pandas as pd
import read_data as read

df_train = read.read_data_to_train_df()
df_ideal = read.read_data_to_ideal_df()
df_test = read.read_data_to_test_df()

def define_deviation():
    print('Display deviation')
    # Sort the df_test by the 'x' column
    sorted_test_df = df_test.sort_values(by='x')
    #export x and y24 from df_ideal
    df2_ideal = pd.DataFrame(zip(df_ideal['x'], df_ideal['y24']))
    # Merge the 'ideal' and 'test' DataFrames based on the common 'x' values
    df_result = pd.merge(sorted_test_df, df_ideal, on='x')
    # Drop the unnecessary columns except x, y and y24 as it's no longer needed
    result_df = df_result.drop(columns=['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11',
           'y12', 'y13', 'y14', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21',
           'y22', 'y23',  'y25', 'y26', 'y27', 'y28', 'y29', 'y30', 'y31',
           'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y40', 'y41',
           'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y50'])
    #Calculate as new column 'deviation'= y-y24
    result_df['deviation'] = result_df['y'] - result_df['y24']
    print(result_df)