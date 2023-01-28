import pandas as pd
from datetime import datetime
import glob
import math
import os

'''

:return: 
'''
def load_all_data():
    """ load all data from 'csv' folder
    :return: dataframe with all the data
    """

    csv_files = glob.glob(os.path.join(os.path.join(os.getcwd(), "csv"), "*.csv"))
    fund_arr = []
    for fnd in csv_files:
        tmp_fund = load_single_data(fnd)
        fund_arr.append(tmp_fund)
    return pd.concat(fund_arr)


def load_single_data(file_path):
    """ load each file
    :param file_path: path to the desired file
    :return: dataframe
    """

    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-8")
    except:
        df = pd.read_csv(file_path)

    df2 = preprocess_data(df)

    print("loaded: " + file_path)
    return df2

def preprocess_data(df, classification="קופת גמל להשקעה"):
    """ pre-process the dataframe
    :param df: dataframe to process
    :param classification: the classification of the fund
    :return: dataframe ready for analyse
    """

    # filter only classification type
    df2 = df[df["FUND_CLASSIFICATION"] == classification]

    # filter column and change column names
    df2 = df2[["FUND_NAME", "MANAGING_CORPORATION", "REPORT_PERIOD",
               "SPECIALIZATION", "MONTHLY_YIELD", "ALPHA", "SHARPE_RATIO",
               "YIELD_TRAILING_3_YRS", "YIELD_TRAILING_5_YRS", "DEPOSITS",
               "WITHDRAWLS", "AVG_ANNUAL_MANAGEMENT_FEE"]]
    df2.columns = ["name", "company", "date",
                   "type", "yield", "alpha", "sharp",
                   "yield3", "yield5", 'deposits',
                   'withdrawls', 'fee']

    # change date to datetime type
    date_str = [str(w) + '01' for w in df2['date'].tolist()]
    df2['date'] = [datetime.strptime(s, '%Y%m%d') for s in date_str]
    # strip name value
    df2['name'] = [b.strip() for b in df2['name'].tolist()]

    # add ration between deposits and withdrawls in [dB]
    deposits = df2['deposits'].tolist()
    deposits = [wd if wd > 0 else 0.0001 for wd in deposits]
    withdrawls = df2['withdrawls'].tolist()
    withdrawls = [wd if wd > 0 else 0.0001 for wd in withdrawls]
    df2['in_out_ratio'] = [10 * math.log10(deposits[i] / withdrawls[i]) for i in range(len(deposits))]

    return df2