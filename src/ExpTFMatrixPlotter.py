__author__ = 'Jonathan Rubin'

import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
from scipy.cluster.hierarchy import dendrogram,linkage
import math

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
            #if float(pval) < pvalcutoff:
            #    pval = 1
            #else:
            #    pval = 0
            if float(pval) == 0:
                pval = pow(10,-200)
            masterdict[exp].append((TF,math.log(float(pval),10)))
    
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
    
    #Generate activity vectors for each TF based on exporder
    vectors = list()
    for tuple1 in TForder:
        TF = tuple1[0]
        explist = list()
        for tuple2 in exporder:
            exp = tuple2[0]
            for tuple3 in masterdict[exp]:
                if tuple3[0]==TF:
                    explist.append(tuple3[1])
        vectors.append(explist)
    
    
    return exporder1,TForder1,vectors
    
if __name__ == "__main__":
    #Specify location of master file. Must be in format: 'Exp\tTF\tpval\tTF\tpval...etc'
    masterfile = 'C:/cygwin64/home/Jonathan/ExpTFMatrixMasterFile.txt'
    #Specify pvalue cutoff to determine whether TF is 'active'
    pvalcutoff = pow(10,-3)
    
    exporder,TForder,vectors = run(masterfile,pvalcutoff)
    vectors = np.array(vectors)
    d = np.zeros((vectors.shape[1],vectors.shape[1]))
    print d.shape
    for i in range(vectors.shape[1]):
        for j in range(vectors.shape[1]):
            d[i,j] = np.sum(np.abs(vectors[:,i]-vectors[:,j]))
    y=linkage(d,method="average")
    z=dendrogram(y,no_plot=True)
    idx=z["leaves"]
    vectors=vectors[:,idx]
            
            
            
    F=plt.figure(figsize=(15,10))
    ax=F.add_axes([0.07,0.1,0.7,0.7])
    
    heatmap = ax.pcolor(vectors, cmap=plt.cm.YlOrBr, alpha=0.8, vmin=-200,vmax=0)
    fig = plt.gcf()
    
    
    # turn off the frame
    ax.set_frame_on(False)
    
    # put the major ticks at the middle of each cell
    res = 7
    ax.set_yticks(np.arange(0,vectors.shape[0],res))
    print len(np.arange(0,vectors.shape[0],res))
    ax.set_xticks(np.arange(vectors.shape[1]) + 0.5, minor=False)
    
    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.yaxis.tick_right()
    ax.xaxis.tick_top()
    
    # note I could have used nba_sort.columns but made "labels" instead
    ax.set_xticklabels(["".join(e.split("bidir")[0].strip('_')) for e in exporder], minor=False,fontsize = 10)
    ax.set_yticklabels([",".join([ TForder[j] for j in range(i,min(i+res, vectors.shape[0]) ) ]) for i in np.arange(0,vectors.shape[0], res)], minor=False,fontsize = 10)
    
    # rotate the
    plt.xticks(rotation=90)
    
    ax.grid(False)
    
    # Turn off all the ticks
    ax = plt.gca()
    
    for t in ax.xaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    
    fig.set_size_inches(20, 15,forward=True)
    plt.savefig('C:/cygwin64/home/Jonathan/BidirectionalTFAnalyzer/images/ExpTFMatrixFig.png')
    plt.show()