__author__ = 'Jonathan Rubin'

import os
import Functions

if __name__ == "__main__":
    directory = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    
    for TF in os.listdir(directory):
        print TF
        if os.path.exists(directory + '/' + TF + '/peak_files/outfiles/MEME'):
            fimocatdir = directory + '/' + TF + '/peak_files/outfiles/MEME/fimo.cat.txt'
            Functions.
            os.system("bedtools merge -i " + fimocatdir + " > fimo.cat.merge.txt")