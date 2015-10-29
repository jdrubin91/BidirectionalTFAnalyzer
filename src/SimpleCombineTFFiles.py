__author__ = 'Jonathan Rubin'

import os
import Functions

def run(RNASeq, Bidir):
    file1 = open(RNASeq)
    file1.readline()
    CombinedDict = dict()
    for line in file1:
        TF,coverage = line.strip().split()
        CombinedDict[TF] = [coverage]
        
    file2 = open(Bidir)
    file2.readline()
    for line in file2:
        TF,pval,cen0,bimod = line.strip().split()[0:5]
        CombinedDict[TF].append((pval,cen0,bimod))
        
    return CombinedDict
    
if __name__ == "__main__":
    Bidir = '/projects/dowellLab/TFIT/Allen2014/FIMO_OUT/Allen2014_DMSO2_3-1_bidirectional_hits_intervals.txt'
    RNASeq = '/scratch/Users/joru1876/BidirectionalTFAnalyzer/files/RNASeqTFLevels.txt'
    
    CombinedDict = run(RNASeq,Bidir)
    
    outfile = open('/scratch/Users/joru1876/BidirectionalTFAnalyzer/files/RNASeqTFLevels.txt','w')
    outfile.write("TF\tRNA-Seq reads\tUniform\tCenter=0\tBimodal\n")
    for TF in CombinedDict:
        outfile.write(TF + "\t")
        for item in CombinedDict[TF]:
            outfile.write(item + "\t")
        outfile.write("\n")