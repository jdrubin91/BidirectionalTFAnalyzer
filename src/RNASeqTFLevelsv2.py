__author__ = 'Jonathan Rubin'

import Functions
import node
import sys
import string

#This code will take a file with gene names for TFs, search for the chromosomal 
#locations of these TF genes using a annotated reference file and return number 
#of reads from an RNA-Seq bedgraph file
def run(TFGeneNames, refFile):
    file1 = open(TFGeneNames)
    file1.readline()
    TFGenesDict = dict()
    for line in file1:
        line = line.strip().split()
        TF, geneNames = line[1][0:line[1].index('_')],line[3:len(line)]
        TFGenesDict[TF] = geneNames
        
    file2 = open(refFile)
    refDict = dict()
    for line in file2:
        line = line.strip().split()
        chrom = line[0]
        start, stop = line[3:5]
        coverage = line[5]
        gene = line[line.index('gene_name')+1]
        gene = ''.join([gene[i] for i in range(0,len(gene)) if gene[i] not in string.punctuation])
        if gene in refDict:
            refDict[gene].append((chrom,start,stop,coverage))
        else:
            refDict[gene] = [(chrom,start,stop,coverage)]
        
    TFCoverage = dict()
    for TF in TFGenesDict:
        for gene in TFGenesDict[TF]:
            if gene in refDict:
                coverage = refDict[gene][0][3]
                TFCoverage[TF] = [coverage]

    
    return TFCoverage

if __name__ == "__main__":
    TFGeneNames = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO/HOCOMOCOGeneNames.txt'
    refFile = '/scratch/Users/joru1876/HCT116RNASeq.gtf'
    
    TFCoverage = run(TFGeneNames, refFile)
    
    outfile = open('/scratch/Users/joru1876/BidirectionalTFAnalyzer/files/RNASeqTFLevels.txt','w')
    outfile.write("TF\tRNA-Seq reads\n")
    for TF in TFCoverage:
        outfile.write(TF + "\t" + TFCoverage[TF][0] + "\n")
    