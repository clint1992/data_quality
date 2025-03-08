import os
import pandas as pd
import numpy as np


def execute():
    print("starting execution")
    # dictionary with data
    d = {'id':1200, 'name':'ramu', 'salary':19920}

    df = pd.DataFrame(d.items())

    print(df.head())



if __name__=='__main__':
    print('Starting main')
    execute()
    print('done')
