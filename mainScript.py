import pickle
import os
import numpy as np
from loadData import load_all_data, load_single_data
from visulizeData import plot_funds, print_list

os.system('cls')
df_all_funds = load_all_data()
names_unique = df_all_funds['name'].unique().tolist()

os.system('cls')
print_list(names_unique)
names_ind = [int(num) for num in input('select funds >>').split(' ')]
fund_names = [names_unique[nm] for nm in names_ind]
df_selected = df_all_funds[df_all_funds['name'].isin(fund_names)]

column_names = df_selected.columns.values.tolist()

os.system('cls')
column_indexes = np.arange(4,len(column_names))
while True:
    print_list(column_names, indexes=column_indexes)
    col_ind_str = input("select data to print ([q] to quit)>>")
    os.system('cls')
    if col_ind_str == 'q':
        break

    if int(col_ind_str) not in column_indexes:
        print("option not in range")
        continue

    plot_funds(df_selected, data_type=column_names[int(col_ind_str)])