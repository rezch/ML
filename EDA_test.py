###
# To run use this in directory :
# python -m IPython EDA_test.py
#
# !!!
#  Always have a folder "results" in proggram directory
# !!!
###

import sys
import numpy as np
import pandas as pd
from time import time
from datetime import datetime
from json import dump
import multitasking

import sweetviz as svz
from autoviz.AutoViz_Class import AutoViz_Class
print('-----------------------------------------------')
print()
print("-Libs imported")

multitasking.set_max_threads(10)
cols = 12
rows = 100
results = {
    'av': 'None',
    'sv': 'None',
    'data': (100000, 12),
           }

class Timer:
    def __init__(self):
        self.start = time()
    
    def end(self):
        return time() - self.start     


# data creating
def data_create():
    df = pd.DataFrame(np.random.rand(rows*1000, 12))
    df.to_csv('data.csv', index=False)
    print()
    print('-Data created')
    print(df.shape[0], df.shape[1])
    results['data'] = (df.shape[0], df.shape[1])
    del df


# sv
@multitasking.task
def sv():
    print()
    print('-SV started')
    timer = Timer()
    df = pd.read_csv('data.csv')
    report = svz.analyze(df)
    report.show_html()
    end = timer.end()
    results['sv'] = end
    print('--- time: ', end)
    print('Result saved in SWEETZ_REPORT.html')
    print('# ',  end='')


# saving
def save():
    print()
    dump(
        results,
        open('results/result_'+str(datetime.now())[:19].replace(':', '-')+".json", 'w')
        )
    print('-Save completed')


# AutoViz
@multitasking.task
def av():
    print()
    print('-AutoZiz started')
    AV = AutoViz_Class()
    
    timer = Timer()
    dft = AV.AutoViz(   # use ipython
        "data.csv",
        sep=",",
        depVar="",
        dfte=None,
        header=0,
        verbose=0,
        lowess=False,
        chart_format="PNG",
        max_rows_analyzed=150000,
        max_cols_analyzed=12,
    )
    end = timer.end()
    results['av'] = end
    print('# ',  end='')



if __name__ == '__main__':
    while True:
        inp = input("# ")
        if inp == 'sv':
            sv()
        elif inp == 'av':
            av()
        elif inp == 'save':
            save()
        elif inp == 'data':
            data_create()
        else:
            try:
                inp = inp.split()
                if inp[0] =='rows':
                    rows = int(inp[1])
                    print('Rows set to', rows*1000)
            except:
                print('Incorrect')
            





    


