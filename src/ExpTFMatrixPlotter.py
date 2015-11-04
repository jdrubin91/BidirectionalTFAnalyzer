__author__ = 'Jonathan Rubin'

import matplotlib
from operator import itemgetter

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
    
    #Generate activity vectors for each TF based on exporder
    vectors = list()
    for tuple1 in TForder:
        TF = tuple1[0]
        explist = list()
        for tuple2 in exporder:
            exp = tuple2[0]
            for tuple3 in masterdict[exp]:
                if tuple3[0]==TF:
                    if float(tuple3[1]) < pvalcutoff:
                        explist.append(1)
                    else:
                        explist.append(0)
        vectors.append(explist)
    
    
    return exporder,TForder,vectors
    
if __name__ == "__main__":
    #Specify location of master file. Must be in format: 'Exp\tTF\tpval\tTF\tpval...etc'
    masterfile = '/scratch/Users/joru1876/ExpTFMatrixMasterFile.txt'
    #Specify pvalue cutoff to determine whether TF is 'active'
    pvalcutoff = 0.0001
    
    exporder,TForder,vectors = run(masterfile,pvalcutoff)
    
    print exporder,TForder,vectors