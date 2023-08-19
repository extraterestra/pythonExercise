import pandas as pd
import numpy as np
import read_data as read

df_train = read.read_data_to_train_df()
df_ideal = read.read_data_to_ideal_df()
df_test = read.read_data_to_test_df()

# Choosing 4 best fit functions from 50 ideal functions similar to 4 train functions
def define_optimal_from_ideal_to_train():
  print('Best fit ideal function')
  for i in range(4):
    y_data = df_train['y' + str(i + 1)]
    best = dict()

    for u in range(50):
      ssr_y = np.sum((y_data - df_ideal['y' + str(u + 1)]) ** 2)
      best['y' + str(u + 1)] = ssr_y

    a = 'y' + str(i + 1)
    b = min(best, key=best.get)
    print(a, b)
