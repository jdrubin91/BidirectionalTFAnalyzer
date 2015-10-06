__author__ = 'Jonathan Rubin'

import os
import Functions

##Runs MEME-ChIP on ConsolidatedPeaks.fasta files to obtain motifs as well as motif locations in genome (located in fimo_out folders). Stores output in MEME folder

#Takes in directory with all TFs and max sites to input into meme
def run(directory, maxsites, tomtomdir):
    directorylist = Functions.chip_peak_directories(directory)
    for item in directorylist:
        if os.path.exists(item + "/outfiles"):
            os.chdir(item + "/outfiles")
            os.system("meme-chip ConsolidatedPeaks.merge.fasta -oc ./MEME meme-maxsites " + str(maxsites))
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
    