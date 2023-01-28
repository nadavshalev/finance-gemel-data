import matplotlib.pyplot as plt
import numpy as np

def print_list(arr, indexes=None):
    """ print list with numbers: [1]  item
    :param arr: list to print
    :param indexes: list off relevant indexes
    """

    if indexes is None:
        indexes = np.arange(len(arr))
    b = ["[" + str(nm) + "]" for nm in indexes]
    c = [b[i] + '\t' + arr[ind] for i,ind in enumerate(indexes)]
    print('\n'.join(c))

def plot_funds(df_funds, data_type):
    """ plot graph of fund data
    :param df_funds: dataframe with funds to plot
    :param data_type: data to plot in Y axis
    """

    gb_funds = df_funds.groupby('name')

    fig, ax = plt.subplots(figsize=(8, 6))

    for label, df in gb_funds:
        df.plot(x='date', y=data_type, ax=ax, label=label[::-1])
    plt.legend()
    plt.title(data_type)

    plt.show(block=True)