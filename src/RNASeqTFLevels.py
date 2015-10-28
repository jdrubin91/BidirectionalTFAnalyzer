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
        TF, geneNames = line[1],line[3:len(line)]
        TFGenesDict[TF] = geneNames
        
    file2 = open(refFile)
    refDict = dict()
    for line in file2:
        line = line.strip().split()
        chrom, start, stop = line[0:3]
        gene = line[line.index('gene_id')+1]
        gene = ''.join([gene[i] for i in range(0,len(gene)) if gene[i] not in string.punctuation])
        if gene in refDict:
            refDict[gene].append((chrom,start,stop))
        else:
            refDict[gene] = [(chrom,start,stop)]
        
    RNASeqDict = Functions.create_bedgraph_dict(RNASeqFile, False)
    
    

    
    
    for TF in TFGenesDict:
        for gene in TF:
            if gene in refDict:
                exonLength = 0
                for site in refDict[gene]:
                    chrom, start, stop = site
                    start = float(start)
                    stop = float(stop)
                    exonLength += stop-start
                    if chrom in RNASeqDict:
                        tree = RNASeqDict[chrom]
                        tree = node.tree(tree)
                        peakval = 0
                        for item in tree.searchInterval((start,stop)):
                            peakval += item[2]
                    TFGenesDict[TF].append(peakval/exonLength)
    
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
    