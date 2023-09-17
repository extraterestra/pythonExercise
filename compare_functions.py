import numpy as np
import pandas as pd
import extract_deviation as deviation
from function_ideal import Function_ideal
from function_test import Function_test

# Choosing 4 best fit functions from 50 ideal functions similar to 4 train functions
def define_optimal_from_ideal_to_train(df_train, df_ideal, df_test):
  result_df = pd.DataFrame(columns=['y_train','y_optimal','deviation'])
  for i in range(4):
    y_data = df_train['y' + str(i + 1)]
    best = dict()

    for u in range(50):
      ssr_y = np.sum((y_data - df_ideal['y' + str(u + 1)]) ** 2)
      best['y' + str(u + 1)] = ssr_y

    num_ideal_function = min(best, key=best.get)
    num_test_function = 'y' + str(i + 1)

    ideal_function = Function_ideal(num_ideal_function,   deviation.define_sum_deviation_for_function(num_ideal_function, df_test, df_ideal))
    test_function = Function_test(num_test_function)

    # Define the new row to be added
    new_row = {'y_train': test_function.num_y_test, 'y_optimal': ideal_function.num_y_ideal, 'deviation': ideal_function.deviation_to_test}

    # Use the loc method to add the new row to the DataFrame
    result_df.loc[len(result_df)] = new_row

  return result_df

def get_best_function(df):
  min_deviation = df.deviation.max()
  row = df.loc[df['deviation'] == min_deviation]
  return row["y_optimal"][1]
