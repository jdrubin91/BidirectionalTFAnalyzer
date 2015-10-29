__author__ = 'Jonathan Rubin'

import Functions
import node
import sys
import string

#This code will take a file with gene names for TFs, search for the chromosomal 
#locations of these TF genes using a annotated reference file and return number 
#of reads from an RNA-Seq bedgraph file
def run(TFGeneNames, refFile, RNASeqFile):
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
        
    print "refDict:",refDict
    

    
    

    
    
    for TF in TFGenesDict:
        print TF
        for gene in TF:
            if gene in refDict:
                TFGenesDict[TF].append(refDict[gene][3])
    
    return TFGenesDict

if __name__ == "__main__":
    TFGeneNames = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO/HOCOMOCOGeneNames.txt'
    refFile = '/scratch/Shares/pubgro/genomefiles/human/hg19.refGene.gtf'
    RNASeqFile = sys.argv[1]
    
    TFGenesDict = run(TFGeneNames, refFile, RNASeqFile)
    
    outfile = open('../files/RNASeqTFLevels.txt','w')
    outfile.write("TF\tRNA-Seq reads")
    for TF in TFGenesDict:
        outfile.write(TF + "\t" + TFGenesDict[TF][1] + "\n")
    