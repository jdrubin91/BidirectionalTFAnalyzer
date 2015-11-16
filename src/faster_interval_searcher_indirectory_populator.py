__author__ = 'Jonathan Rubin'

import os
import Functions


#Takes all ChIP peak files, if there is a corresponding fimo file, add both to 
#outdirectory. This script prepares outdirectory for use with fast-er_interval_searhcer    
if __name__ == "__main__":
    chipdir = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    fimodir = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_Files'
    outdirectory = '/scratch/Users/joru1876/fast-er_inteval_searcher/HCT116_Chip_FIMO'
    
    for TF in os.listdir(chipdir):
        newdir = chipdir + '/' + TF + '/peak_files'
        newdir = newdir + [i for i in os.listdir(newdir) if 'ENC' in i][0]
        for fimo in os.listdir(fimodir):
            if TF in fimo:
                os.system("cat " + newdir + " > " + outdirectory + "/" + TF + ".bed")
                os.systme("scp " + fimodir + "/" + fimo + " " + outdirectory)
        