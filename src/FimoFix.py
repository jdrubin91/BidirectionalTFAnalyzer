__author__ = 'Jonathan Rubin'

import os
import Functions

##Removes duplicates and creates non-overlapping intervals for FIMO files

def run(directory):
    directorylist = Functions.fimo_directories(directory)
    for item in directorylist:
        os.chdir(item)
        FileList = Functions.parse_file("fimo.txt")
        Functions.cut_file("fimo.txt", [i for i in range(1,len(FileList[0]))], "fimo.cut.bed")
        Functions.remove_duplicates_int("fimo.cut.bed", "fimo.cut.rmdup.bed", True)
        Functions.order_file("fimo.cut.rmdup.bed", "fimo.cut.rmdup.ord.bed", True)
        Functions.replace_header("fimo.cut.rmdup.ord.bed", "#chrom\tstart\tstop\tstrand")
        os.system("bedtools merge -i fimo.cut.rmdup.ord.bed > fimo.cut.rmdup.ord.merge.bed")

        
if __name__ == "__main__":
    directory = "/projects/dowellLab/ENCODE/HL60"
    directorylist = Functions.fimo_directories(directory)
    for item in directorylist:
        os.chdir(item)
        FileList = Functions.parse_file("fimo.txt")
        Functions.cut_file("fimo.txt", [i for i in range(1,len(FileList[0]))], "fimo.cut.bed")
        Functions.remove_duplicates_int("fimo.cut.bed", "fimo.cut.rmdup.bed", True)
        Functions.order_file("fimo.cut.rmdup.bed", "fimo.cut.rmdup.ord.bed", True)
        Functions.replace_header("fimo.cut.rmdup.ord.bed", "#chrom\tstart\tstop\tstrand")
        os.system("bedtools merge -i fimo.cut.rmdup.ord.bed > fimo.cut.rmdup.ord.merge.bed")

        
        
        