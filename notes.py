#https://www.zipline.io/beginner-tutorial.html#basics

## About
'''
    Zipline is an open-source algorithmic trading simulator written in Python.
    Source Code: https://github.com/quantopian/zipline
'''

## Install
'''
pip install zipline
conda install -c Quantopian zipline -c quantopian ta-lib

or even better create enviroment with Zipline
conda create -n zipline_env -c Quantopian zipline -c quantopian ta-libc
(to activate:   $source activate zipline_env)
(to deactivate: $ source deactivate)
'''

######### BASICS ############################
'''
Every zipline algorithm consists of two functions you have to define:
    -initialize(context)
    -handle_data(context, data)
'''
## Example: buyapple.py
import sys
from zipline.examples import buyapple
from zipline.api import order, record, symbol

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))
'''
After the algorithm finished running you will have access to each variable value you tracked with record()
'''

## Ingesting Data
'''
check pricing data(data bundles):
$ zipline bundles

To ingest data
$ QUANDL_API_KEY=<yourkey> zipline ingest [-b <bundle>]
$ QUANDL_API_KEY=EU2L5gfLyQdnJQd9SpLR zipline ingest -b quantopian-quandl
This will be written in $ZIPLINE_ROOT/data/<bundle> where by default ZIPLINE_ROOT=~/.zipline
'''


## Running
'''
...and save the results to buyapple_out.pickle

$ zipline run -f ../../zipline/examples/buyapple.py --start 2016-1-1 --end 2018-1-1 -o buyapple_out.pickle
$ zipline run -f notes.p --start 2016-1-1 --end 2018-1-1 -o buyapple_out.pickle
or
$zipline run --bundle quantopian-quandl -f apple_backtest.py --start 2000-1-1 --end 2018-1-1 --output buyapple_out.pickle

or in an Ipython Notebook
%zipline --bundle quantopian-quandl --start 2008-1-1 --end 2012-1-1 -o dma.pickle
%zipline --bundle quantopian-quandl --start 2000-1-1 --end 2012-1-1 -o backtest.pickle
'''
