'''
Created on Nov 21, 2012

@author: sscepano
'''

# This one serves for reading in data in full --- for finding number of users, user homes etc
from collections import defaultdict 
from multiprocessing import Pool
import logging
import numpy as n
import traceback

from read_in import data as rd
from analyze import test_data as a


_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')
    
    C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    data = defaultdict(int)
    for c in C:
        data = rd.read_in_file(c, data)
    
    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            #reload(rd)
            reload(a)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            a.print_data_stats(data)
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()