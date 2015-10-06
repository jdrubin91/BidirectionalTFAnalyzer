__author__ = 'Jonathan Rubin'

import Functions
import os

##Converts ConsolidatedPeaks.merge.bed file from ChipRepConsolidater to Fasta format (ConsolidatedPeaks.fasta) in preparation for MEME-CHIP

def run(directory, referencefilepath):
    directorylist = Functions.chip_peak_directories(directory)
    for item in directorylist:
        if os.path.exists(item + "/outfiles"):
            os.chdir(item + "/outfiles")
            os.system("bedtools getfasta -fi " + referencefilepath + " -bed ConsolidatedPeaks.merge.bed -fo ConsolidatedPeaks.merge.fasta")
        else:
            print "File not found in: " + item
        
if __name__ == "__main__":
    directory = "/projects/dowellLab/ENCODE/HL60"
    referencefilepath = "/Users/joru1876/hg19_reference_files/hg19v1/uncompressed/hg19_whole_genome.fa"
    directorylist = Functions.chip_peak_directories(directory)
    for item in directorylist:
        os.chdir(item + "/outfiles")
        os.system("bedtools getfasta -fi " + referencefilepath + " -bed ConsolidatedPeaks.merge.bed -fo ConsolidatedPeaks.merge.fasta")