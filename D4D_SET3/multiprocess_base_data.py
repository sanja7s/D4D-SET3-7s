'''
Created on Nov 21, 2012

@author: sscepano
'''

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
    
#    dataA = defaultdict(int)
#    dataA = rd.read_in_file('A', dataA)
#    
#    dataB = defaultdict(int)
#    dataB = rd.read_in_file('B', dataB)
#    
#    dataC = defaultdict(int)
#    dataC = rd.read_in_file('C', dataC)
#    
#    dataD = defaultdict(int)
#    dataD = rd.read_in_file('D', dataD)
#    
#    dataE = defaultdict(int)
#    dataE = rd.read_in_file('E', dataE)
#    
#    dataF = defaultdict(int)
#    dataF = rd.read_in_file('F', dataF)
#    
#    dataG = defaultdict(int)
#    dataG = rd.read_in_file('G', dataG)
#    
#    dataH = defaultdict(int)
#    dataH = rd.read_in_file('H', dataH)
#    
#    dataI = defaultdict(int)
#    dataI = rd.read_in_file('I', dataI)
#    
#    dataJ = defaultdict(int)
#    dataJ = rd.read_in_file('J', dataJ)
    
    p = Pool(10)
    
    p.map(rd.read_in_file_multiprocessing, C)
    
    
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
            data = a.sum_data(dataA, dataB, dataC, dataD, dataE, dataF, dataG, dataH, dataI, dataJ)
            a.print_data_stats(data)
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()

