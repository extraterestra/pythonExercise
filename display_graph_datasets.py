import matplotlib.pyplot as plt

def show_graph(df_train, df_test, df_ideal):
    # Set up the figure and axes
    fig, axs = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Functions Visualization', fontsize=16)

    # Plot y13
    axs[0, 0].plot(df_train['x'], df_ideal['y13'], color='red', marker='o', linestyle='', linewidth=2)
    axs[0, 0].plot(df_train['x'], df_train['y1'], color='blue', marker='o', linestyle='', linewidth=2)
    axs[0, 0].set_title('Function x(y13)')

    # Plot y2(train) to y24(ideal)
    axs[0, 1].plot(df_train['x'], df_train['y2'], color='blue', marker='o', linestyle='', linewidth=2)
    axs[0, 1].plot(df_train['x'], df_ideal['y24'], color='red', marker='o', linestyle='', linewidth=1)
    axs[0, 1].set_title('Function x(y24)')

    # Plot y3(train) to y36(ideal)
    axs[1, 0].plot(df_train['x'], df_train['y3'], color='blue', marker='o', linestyle='', linewidth=2)
    axs[1, 0].plot(df_train['x'], df_ideal['y36'], color='red', marker='o', linestyle='', linewidth=2)
    axs[1, 0].set_title('Function x(y36)')

    # Plot y4(train) to y40(ideal)
    axs[1, 1].plot(df_train['x'], df_train['y4'], color='blue', marker='o', linestyle='', linewidth=2)
    axs[1, 1].plot(df_train['x'], df_ideal['y40'], color='red', marker='o', linestyle='', linewidth=2)
    axs[1, 1].set_title('Function x(y40)')

    # Plot y4(train) to y40(ideal)
    axs[0, 2].plot(df_train['x'], df_ideal['y13'], color='red', marker='o', linestyle='', linewidth=2)
    axs[0, 2].plot(df_train['x'], df_ideal['y24'], color='red', marker='o', linestyle='', linewidth=2)
    axs[0, 2].plot(df_train['x'], df_ideal['y36'], color='red', marker='o', linestyle='', linewidth=2)
    axs[0, 2].plot(df_train['x'], df_ideal['y40'], color='red', marker='o', linestyle='', linewidth=2)
    axs[0, 2].plot(df_test['x'], df_test['y'], color='blue', marker='o', linestyle='', linewidth=2)
    axs[0, 2].set_title('Function test x(y) and four best fit ideal functions')

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()
