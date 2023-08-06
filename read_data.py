import sqlite3
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def connect_to_db():
    conn = sqlite3.connect('my_data.db')
    conn.cursor()
    return conn
def read_data_to_test_df():
    conn = connect_to_db()
    test_df = pd.read_sql('''SELECT * FROM test''', conn)
    return test_df

def read_data_to_train_df():
    conn = connect_to_db()
    train_df = pd.read_sql('''SELECT * FROM train''', conn)
    return train_df

def read_data_to_ideal_df():
    conn = connect_to_db()
    ideal_df = pd.read_sql('''SELECT * FROM ideal''', conn)
    return ideal_df

# print('SHAPE OF DF IDEAL')
# print(read_data_to_ideal_df().shape)
#
# print('SHAPE OF DF TRAIN')
# print(read_data_to_train_df().shape)
#
# print('SHAPE OF DF TEST')
# print(read_data_to_test_df().shape)




# test_df.shape
# train_df.shape
# ideal_df.shape
#
# print('SHAPE OF DF TRAIN')
# print(train_df.shape)
#
# print('SHAPE OF DF TEST')
# print(test_df.shape)
#
# print('SHAPE OF DF IDEAL')
# print(ideal_df.shape)



# Step 1: Extract the column data as a Pandas Series
# column_x_data_series = train_df['x']
# column_y_data_series = train_df['y']

# # Step 2: Convert the Pandas Series to a NumPy array
# data_array_x = column_x_data_series.values
# data_array_y = column_y_data_series.values
#
# print('ARRAY Y')
# print(data_array_y)
# print('ARRAY X')
# print(data_array_x)
#
# # Perform cubic polynomial regression
# coefficients = np.polyfit(data_array_x, data_array_y, 3)
#
# # Print the coefficients
# print("Coefficients test function (a, b, c, d):", coefficients)
#
# # Function to define the ideal function with parameters a, b, c, and d
# # def ideal_function(x, a, b, c, d):
# #     return a * x**3 + b * x**2 + c * x + d
#
# # Helper function to calculate the sum of squared deviations
# def calculate_sum_squared_deviations(ideal_function, x_train, y_train):
#     y_pred = np.polyval(ideal_function, x_train)
#     deviations = y_pred - y_train
#     return np.sum(deviations ** 2)
#
# # Load the training dataset
# training_data = np.array(train_df)
# # print("The 2D-Array Train dataset: ", training_data)
#
# # Load the test dataset
# test_data_loaded = np.array(test_df)
# # print("The 2D-Array Test dataset: ", test_data_loaded)
#
# # Load the ideal functions dataset
# ideal_functions = np.array(ideal_df)
# # print("The 2D-Array Ideal functions dataset: ", ideal_functions)
#
# # Split the training dataset into x and y values
# x_train = training_data[:, 0]
# y_train = training_data[:, 1:]
#
# print("x_train: ", x_train)
# print("y_train: ", y_train)
#
# # Initialize variables to store the best fit ideal functions
# best_fit_functions = []
# best_fit_deviations = []
#
# # Find the four best fit ideal functions using Least-Square method
# for i in range(4):
#     min_deviation = float('inf')
#     best_function = None
#
#     for ideal_function in ideal_functions:
#         deviation = calculate_sum_squared_deviations(ideal_function, x_train, y_train[:, i])
#         if deviation < min_deviation:
#             min_deviation = deviation
#             best_function = ideal_function
#
#     best_fit_functions.append(best_function)
#     best_fit_deviations.append(min_deviation)
#
# print("Best fit 4 Ideal functions: ", best_fit_functions)
# print("Best fit deviations fo 4 Ideal functions: ", best_fit_deviations)
#
# # Load the test data from the training dataset
# test_data = training_data[:, 0:2]
#
# # Initialize variables to store the mappings and deviations
# mappings = np.zeros((len(test_data), 4))
# test_deviations = np.zeros((len(test_data), 4))
#
# # Map test data using the chosen ideal functions
# for i in range(4):
#     mapped_y = np.polyval(best_fit_functions[i], test_data[:, 0])
#     mappings[:, i] = mapped_y
#     test_deviations[:, i] = np.abs(mapped_y - test_data[:, 1])
#
#
# # Print the best fit ideal functions and their deviations
# for i in range(4):
#     print(f"Ideal Function {i+1} (y{i+1}): {best_fit_functions[i]}")
#     print(f"Deviation for y{i+1}: {best_fit_deviations[i]}")
#     print()
#
#
# # Print the mappings and deviations for each x-y pair in the test data
# # for i in range(len(test_data)):
# #     print(f"Test Data Point {i+1}: x={test_data[i, 0]}, y={test_data[i, 1]}")
# #     for j in range(4):
# #         print(f"   Mapped y{j+1}: {mappings[i, j]}, Deviation: {test_deviations[i, j]}")
# #     print()
#
#
# # Find the one best fit ideal functions using Least-Square method from 4 best fit ideal functions
# # TODO
#
#
# # Visualize the best fit ideal functions and their deviations
#
# # Plot the best fit ideal functions
# plt.figure(figsize=(12, 8))
# for i in range(4):
#     plt.plot(x_train, np.polyval(best_fit_functions[i], x_train), label=f"Ideal Function {i+1}")
#
# plt.scatter(x_train, y_train[:, 0], color='red', label='Train Data (y1)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Best Fit Ideal Functions')
# plt.legend()
# plt.grid()
# plt.show()
#
# # Plot the deviations for each chosen ideal function
# plt.figure(figsize=(12, 8))
# for i in range(4):
#     plt.plot(x_train, np.abs(np.polyval(best_fit_functions[i], x_train) - y_train[:, i]), label=f'Deviation (y{i+1})')
#
# plt.xlabel('x')
# plt.ylabel('Deviation')
# plt.title('Deviations for Chosen Ideal Functions')
# plt.legend()
# plt.grid()
# plt.show()