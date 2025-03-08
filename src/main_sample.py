
import os

import numpy as np
import pandas as pd


def execute():
    import datetime
    print("starting execution")
    # dictionary with data
    d = {'id':1200, 'name':'ramu', 'salary':19920}

    df = pd.DataFrame(d.items())

    print(df.head())



if __name__=='__main__':
    print('Starting main')
    execute()
    print('done')
