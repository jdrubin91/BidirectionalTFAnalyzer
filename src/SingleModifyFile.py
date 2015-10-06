__author__ = 'Jonathan Rubin'

import os
import sys
import Functions
            

if __name__ == "__main__":
    
    file1 = sys.argv[1]
    
    Functions.cut_file(file1, [1,2,3], Functions.get_mod_filename(file1,'cut'))
    
