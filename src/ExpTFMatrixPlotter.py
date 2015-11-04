__author__ = 'Jonathan Rubin'

import matplotlib

def run(masterfile,pvalcutoff):
    #Takes as input a master file with format 'Exp\tTF\tpval\tTF\tpval...etc'
    #Returns three ordered lists ([exp],[TF],[TF vals])
    masterdict = dict()
    for line in open(masterfile):
        linetabsplit = line.strip().split()
        exp = linetabsplit[0][0:linetabsplit[0].index('.')]
        masterdict[exp] = list()
        linecommasplit = linetabsplit[1].split(',')
        for i in range(0,len(linecommasplit),2):
            TF = linecommasplit[i]
            pval = linecommasplit[i+1]
            if pval < pvalcutoff:
                pval = 1
            else:
                pval = 0
            masterdict[exp].append((TF,pval))
            
    
    return masterdict
    
if __name__ == "__main__":
    #Specify location of master file. Must be in format: 'Exp\tTF\tpval\tTF\tpval...etc'
    masterfile = '/scratch/Users/joru1876/ExpTFMatrixMasterFile.txt'
    #Specify pvalue cutoff to determine whether TF is 'active'
    pvalcutoff = 0.0001
    
    masterdict = run(masterfile,pvalcutoff)
    
    print masterdict