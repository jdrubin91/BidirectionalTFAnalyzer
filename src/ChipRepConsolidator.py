__author__ = 'Jonathan Rubin'

##Consolidate replicate ChIP peak bed files into a single ConsolidatedPeaks.bed file, then merge file to ensure non-overlapping intervals. If only one replicate, create ConsolidatedPeaks.bed file from single replicate

import Functions
import os

def run(directory):
    directorylist = Functions.chip_peak_directories(directory)
    for item in directorylist:
        os.chdir(item)
        FileList = [file1 for file1 in os.listdir(item) if '.bed' in file1]
        if len(FileList) != 0:
            if 'outfiles' not in os.listdir(item):
                os.mkdir("./outfiles")
            if len(FileList) > 1:
                os.system("bedtools intersect -a " + FileList[0] + " -b " + " ".join(FileList[1:len(FileList)]) + " > ./outfiles/ConsolidatedPeaks.bed")
            else:
                os.system("cat " + FileList[0] + " > ./outfiles/ConsolidatedPeaks.bed")
            os.chdir("./outfiles")
            Functions.order_file("ConsolidatedPeaks.bed", "ConsolidatedPeaks.bed", False)
            os.system("bedtools merge -i ConsolidatedPeaks.bed > ConsolidatedPeaks.merge.bed")
        else:
            print "No bed files found in: " + item

        
if __name__ == "__main__":
    directory = "/projects/dowellLab/ENCODE/HL60"
    directorylist = Functions.chip_peak_directories(directory)
    for item in directorylist:
        os.chdir(item)
        FileList = [file1 for file1 in os.listdir(item) if 'bed' in file1]
        if 'outfiles' not in os.listdir(item):
            os.mkdir("./outfiles")
        if len(FileList) > 1:
            os.system("bedtools intersect -a " + FileList[0] + " -b " + " ".join(FileList[1:len(FileList)]) + " > ./outfiles/ConsolidatedPeaks.bed")
        else:
            os.system("cat " + FileList[0] + " > ConsolidatedPeaks.bed")
        os.chdir("./outfiles")
        os.system("bedtools merge -i ConsolidatedPeaks.bed > ConsolidatedPeaks.merge.bed")