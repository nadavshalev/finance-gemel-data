import pickle
import os
import numpy as np
from loadData import load_all_data, load_single_data, get_all_types
from visulizeData import plot_funds, print_list

# select type of fund
os.system('cls')
all_types = get_all_types(os.path.join(os.path.join(os.getcwd(), "csv"), "data_2022_.csv"))
print_list(all_types)
type_ind = int(input('select type of funds >>'))

# load all data
os.system('cls')
df_all_funds = load_all_data(all_types[type_ind])

# select companies
os.system('cls')
company_unique = df_all_funds['company'].unique().tolist()
company_unique.sort()
print_list(company_unique)
company_ind = [int(num) for num in input('select companies >>').split(' ')]
company_names = [company_unique[nm] for nm in company_ind]
df_selected = df_all_funds[df_all_funds['company'].isin(company_names)]

# select funds
os.system('cls')
names_unique = df_selected['name'].unique().tolist()
names_unique.sort()
print_list(names_unique)
names_ind = [int(num) for num in input('select funds >>').split(' ')]
fund_names = [names_unique[nm] for nm in names_ind]
df_selected = df_selected[df_selected['name'].isin(fund_names)]
column_names = df_selected.columns.values.tolist()

# show graphs
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