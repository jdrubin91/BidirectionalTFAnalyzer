__author__ = 'Jonathan Rubin'

import os
import sys
import Functions
            

if __name__ == "__main__":
    
    filepath = sys.argv[1]
    
    for TF in os.listdir(filepath):
        os.chdir(filepath + '/' + TF + '/')
        file1 = 'fimo.txt'
        if os.path.exists(filepath + '/' + TF + '/fimo.txt'):
            Functions.cut_file(file1, [1,2,3,4,5,6,7], Functions.get_mod_filename(file1,'cut'))
    
