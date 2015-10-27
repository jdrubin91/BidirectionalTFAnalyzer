__author__ = 'Jonathan Rubin'

import Functions
import node
import sys

#This code will take a file with gene names for TFs, search for the chromosomal 
#locations of these TF genes using a annotated reference file and return number 
#of reads from an RNA-Seq bedgraph file
def run(TFGeneNames, refFile, RNASeqFile):
    file1 = open(TFGeneNames)
    file1.readline()
    TFGenesDict = dict()
    for line in file1:
        line = line.strip().split()
        TF, geneNames = line[1],line[3:len(line)]
        TFGenesDict[TF] = geneNames
        
    file2 = open(refFile)
    refDict = dict()
    for line in file2:
        chrom, start, stop, gene = line.strip().split()[0:4]
        refDict[gene] = [chrom,start,stop]
        
    RNASeqDict = Functions.create_bedgraph_dict(RNASeqFile, False)
    
    
    
    for TF in TFGenesDict:
        for gene in TF:
            if gene in refDict:
                chrom, start, stop = refDict[gene]
                if chrom in RNASeqDict:
                    tree = RNASeqDict[chrom]
                    tree = node.tree(tree)
                    peakval = 0
                    for item in tree.searchInterval((start,stop)):
                        peakval += item[2]
                TFGenesDict[TF].append(peakval)
    
    return TFGenesDict

if __name__ == "__main__":
    TFGeneNames = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO/HOCOMOCOGeneNames.txt'
    refFile = '/scratch/Users/joru1876/hg19_reference_files/refFlat_hg19.bed'
    RNASeqFile = sys.argv[1]
    
    TFGenesDict = run(TFGeneNames, refFile, RNASeqFile)
    
    outfile = open('RNASeqTFLevels.txt','w')
    outfile.write("TF\tRNA-Seq reads")
    for TF in TFGenesDict:
        outfile.write(TF + "\t" + TFGenesDict[TF][1] + "\n")
    