import pandas as pd
from pathlib import Path


def prepare_data():

    paralympics_raw_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(paralympics_raw_csv)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    return df


if __name__ == '__main__':
    ''' 
    Add a line of code to create a dataframe by reading the file ('data/paralympics_raw.csv') from csv
    
    To use pathlib for the file path: 
    paralympics_raw = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    '''

    # Add code to change the pandas display options for the max_rows and max_columns (optional)
    
    # Add a line of code to print the dataframe contents
    df_raw = prepare_data()
    print(df_raw)
