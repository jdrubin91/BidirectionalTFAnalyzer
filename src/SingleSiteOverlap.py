__author__ = 'Jonathan Rubin'

import os
import sys
import Functions
            

if __name__ == "__main__":
    
    file1 = sys.argv[1]
    header1 = sys.argv[2]
    file2 = sys.argv[3]
    header2 = sys.argv[4]
    file3 = sys.argv[5]
    header3 = sys.argv[6]
    
    print Functions.venn_d3(file1, header1, file2, header2, file3, header3) 

    
