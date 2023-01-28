
import os
from loadData import load_all_data, load_single_data
from visulizeData import plot_funds, print_funds

# for debug only
# load_single_data(os.getcwd() + "\\csv\\data_2021_.csv")

USE_HARDCODED_INDEX = True

df_all_funds = load_all_data()
names_unique = df_all_funds['name'].unique().tolist()

# get specific funds
if USE_HARDCODED_INDEX:
    names_ind = [1, 6, 12, 113, 39]
else:
    print_funds(names_unique)
    names_ind = [int(num) for num in input('>>').split(' ')]
fund_names = [names_unique[nm] for nm in names_ind]

# filter selected funds
df_selected = df_all_funds[df_all_funds['name'].isin(fund_names)]

# plot funds
plot_funds(df_selected, data_type='yield3')
plot_funds(df_selected, data_type='sharp')
