__author__ = 'Jonathan Rubin'

import os
import Functions

##Runs MEME on ConsolidatedPeaks.fasta files to obtain motifs. Stores output in MEME folder

#Takes in directory with all TFs, max size, max sites to input into MEME
def run(directory, maxsize, maxsites, tomtomdir):
    directorylist = Functions.chip_peak_directories(directory)
    for item in directorylist:
        if os.path.exists(item + "/outfiles"):
            os.chdir(item + "/outfiles")
            os.system("meme ConsolidatedPeaks.merge.fasta -dna -oc ./MEME -maxsize " + str(maxsize) + " -maxsites " + str(maxsites))
            os.chdir(item + "/outfiles/MEME")
            os.system("tomtom combined.meme " + tomtomdir)
        else:
            print "File not found in: " + item


if __name__ == "__main__":
    directory = "/projects/dowellLab/ENCODE/HL60"
    directorylist = Functions.chip_peak_directories(directory)
    maxsites = 10000000
    for item in directorylist:
        os.chdir(item + "/outfiles")
        os.system("meme ConsolidatedPeaks.merge.fasta -dna -oc ./MEME meme-maxsites " + str(maxsites))
    