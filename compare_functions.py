import read_data as read
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df_train = read.read_data_to_train_df()
df_ideal = read.read_data_to_ideal_df()
df_train_2 = df_train.iloc[:, :2]

# print(df_train_2)
print(df_train)

ideal_functions = df_ideal
test_function = df_train_2

#Extract column x and y to numpy arrays (from train 4 functions dataset)
x_train = df_train['x'].to_numpy()
y_train = df_train['y1'].to_numpy()

#Extract column x and y to numpy arrays (from IDEAL 50 functions dataset)
x_ideal = df_ideal['x'].to_numpy()
y1 = df_ideal['y1'].to_numpy()
y2 = df_ideal['y2'].to_numpy()
y3 = df_ideal['y3'].to_numpy()


# Fit a linear regression model to (x, y)
model_xy_train = LinearRegression()
model_xy_train.fit(x_train.reshape(-1, 1), y_train)

# Fit a linear regression model to (x_ideal, y_ideal)
model_xy_ideal = LinearRegression()
model_xy_ideal.fit(x_ideal.reshape(-1, 1), y1)

# Fit a linear regression model to (x_ideal, y_ideal)
model_xy_ideal2 = LinearRegression()
model_xy_ideal2.fit(x_ideal.reshape(-1, 1), y2)

# Fit a linear regression model to (x_ideal, y_ideal)
model_xy_ideal3 = LinearRegression()
model_xy_ideal3.fit(x_ideal.reshape(-1, 1), y3)


# Calculate the predicted values for (x, y) and (x1, y1)
y_pred_y = model_xy_train.predict(x_train.reshape(-1, 1))
y_pred_y1 = model_xy_ideal.predict(x_ideal.reshape(-1, 1))
y_pred_y2 = model_xy_ideal2.predict(x_ideal.reshape(-1, 1))
y_pred_y3 = model_xy_ideal3.predict(x_ideal.reshape(-1, 1))

# Calculate the sums of squared residuals (SSR) for each model
ssr_y = np.sum((y_train - y_pred_y) ** 2)
ssr_y1 = np.sum((y1 - y_pred_y1) ** 2)
ssr_y2 = np.sum((y2 - y_pred_y2) ** 2)
ssr_y3 = np.sum((y3 - y_pred_y3) ** 2)

print(f"SSR for (x, y): {ssr_y}")
print(f"SSR for (x1, y1): {ssr_y1}")
print(f"SSR for (x1, y2): {ssr_y2}")
print(f"SSR for (x1, y3): {ssr_y3}")

# Compare the SSR values to find the best fit test function
ssr_values = [ssr_y, ssr_y2, ssr_y2, ssr_y3]
best_fit_index = np.argmin(ssr_values)

print(f"BEST FIT FUNCTION: {best_fit_index + 1}")
best_fit_test_function = [y1, y2, y3][best_fit_index] #y_train,

# Calculate the deviation (delta) for each (x, y) pair of the ideal function
deviation = y_train - best_fit_test_function

# for dev in zip(deviation):
#     print(f"({dev}")

# Output the result
print(f"Best fit test function: (x, y) = (xi, y{best_fit_index + 1})")
print(f"Delta for deviation from the ideal function for each (x, y) pair:")
# for xi_val, yi_val, dev in zip(x_train, y_train, deviation):
    # print(f"({xi_val}, {yi_val}): {dev}")


