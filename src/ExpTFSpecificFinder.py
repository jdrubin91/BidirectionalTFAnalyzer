__author__ = 'Jonathan Rubin'

import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
from scipy.cluster.hierarchy import dendrogram,linkage

def run(masterfile,pvalcutoff):
    #Takes as input a master file with format 'Exp\tTF\tpval\tTF\tpval...etc'
    #Returns three ordered lists ([exp],[TF],[TF vals])
    masterdict = dict()
    for line in open(masterfile):
        linetabsplit = line.strip().split()
        exp = linetabsplit[0][0:linetabsplit[0].index('.')]
        masterdict[exp] = list()
        linecommasplit = linetabsplit[1].split(',')
        for i in range(0,len(linecommasplit)-1,2):
            TF = linecommasplit[i]
            pval = linecommasplit[i+1]
            if float(pval) < pvalcutoff:
                pval = 1
            else:
                pval = 0
            masterdict[exp].append((TF,pval))
    
    #Order experiments by number of active TFs
    exporder = list()
    for key in masterdict:
        size = 0
        for tuples in masterdict[key]:
            size += tuples[1]
        exporder.append((key,size))
    exporder = sorted(exporder,key=itemgetter(1),reverse=True)
    exporder1 = list()
    for item in exporder:
        exporder1.append(item[0])
    
    #Order TFs by times active in exp
    TFdict = dict()
    TForder = list()
    for key in masterdict:
        for tuples in masterdict[key]:
            if tuples[0] not in TFdict:
                TFdict[tuples[0]] = 0
            TFdict[tuples[0]]+=tuples[1]
    for key in TFdict:
        TForder.append((key, TFdict[key]))
    TForder = sorted(TForder,key=itemgetter(1),reverse=True)
    TForder1 = list()
    for item in TForder:
        TForder1.append(item[0])
    
    #Generate dictionary of {TF : [active exps]} 
    explist = dict()
    for tuple1 in TForder:
        TF = tuple1[0]
        for tuple2 in exporder:
            exp = tuple2[0]
            if not TF in explist:
                explist[TF] = list()
            for tuple3 in masterdict[exp]:
                if tuple3[0]==TF:
                    if int(tuple3[1]) == 1:
                        explist[TF].append(exp)
    
    exporder1 = sorted(explist, key=lambda k: len(explist[k]), reverse=True)

    
    
    return exporder1,explist
    
if __name__ == "__main__":
    #Specify location of master file. Must be in format: 'Exp\tTF\tpval\tTF\tpval...etc'
    masterfile = 'C:/cygwin64/home/Jonathan/ExpTFMatrixMasterFile.txt'
    #Specify pvalue cutoff to determine whether TF is 'active'
    pvalcutoff = pow(10,-3)
    
    exporder,explist = run(masterfile,pvalcutoff)
    for key in exporder:
        print key + ":" + exporder[key]
