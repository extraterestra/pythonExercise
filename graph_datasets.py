import read_data as read
import pandas as pd
import matplotlib.pyplot as plt

print('SHAPE OF DF TEST')
print(read.read_data_to_test_df().shape)
print('SHAPE OF DF TRAIN')
print(read.read_data_to_train_df().shape)
print('SHAPE OF DF IDEAL')
print(read.read_data_to_ideal_df().shape)

df_train = read.read_data_to_train_df()
df_test = read.read_data_to_test_df()

# Set up the figure and axes
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Four Functions Visualization', fontsize=16)

# Plot y1
axs[0, 0].plot(df_train['x'], df_train['y1'], color='blue')
axs[0, 0].set_title('Function y1')

# Plot y2
axs[0, 1].plot(df_train['x'], df_train['y2'], color='red')
axs[0, 1].set_title('Function y2')

# Plot y3
axs[1, 0].plot(df_train['x'], df_train['y3'], color='green')
axs[1, 0].set_title('Function y3')

# Plot y4
axs[1, 1].plot(df_train['x'], df_train['y4'], color='purple')
axs[1, 1].set_title('Function y4')

# # Plot test
# axs[1, 1].plot(df_test['x'], df_test['y'], color='black')
# axs[1, 1].set_title('Function Test')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# Create the plot using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df_test['x'], df_test['y'], color='blue', marker='o', linestyle='', linewidth=2)
plt.title('Function y(x)', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.show()