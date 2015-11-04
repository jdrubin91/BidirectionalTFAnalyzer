__author__ = 'Jonathan Rubin'

import Functions
import os

def run(TFITDir):
    #Creates a dictionary with experiments as key followed by list of tuples (TF, pval)
    #returns dictionary
    TFITDict = dict()
    for directory in Functions.TFIT_fimo_directories(TFITDir):
        for bidirfile in os.listdir(directory):
            if 'GSM' not in bidirfile:
                TFITDict[bidirfile] = list()
                file1 = open(directory + '/' + bidirfile)
                file1.readline()
                for line in file1:
                    TF,pval = line.strip().split()[0:2]
                    TFITDict[bidirfile].append((TF,pval))
        
    
    return TFITDict
    
if __name__ == "__main__":
    #Specify directory
    TFITDir = '/scratch/Users/joru1876/TFIT'
    
    TFITDict = run(TFITDir)
    
    os.chdir(Functions.parent_dir(TFITDir))
    outfile = open('ExpTFMatrixMasterFile.txt','w')
    for exp in TFITDict:
        outfile.write(exp)
        outfile.write('\t')
        for val in TFITDict[exp]:
            outfile.write(val)
            outfile.write('\t')
        outfile.write('\n')