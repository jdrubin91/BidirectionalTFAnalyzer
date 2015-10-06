__author__ = 'Jonathan Rubin'

##Main

import sys
import os
import Functions
import Cleaner as cl
import ChipRepConsolidator as rc
import BedToFasta as b2f
import Meme as meme
import FimoFix as ff
import MotifToBidirDistance as dist
import SiteOverlap as so



#Directory containing all TF folders
directory = sys.argv[1]

referencefilepath = sys.argv[2]

#Clean directory beforehand?
boolean = False

def run():
    #Set home directory
    homedir = os.path.dirname(os.path.realpath(__file__))
    #Get full path to reference genome file (must be in files folder)
    #referencefilepath = Functions.parent_dir(homedir) + '/files/hg19_whole_genome.fa'
    #Get full path to bidirectional hits file (must be in files folder)
    bidirectionalfilepath = Functions.parent_dir(homedir) + '/files/bidirectional_hits.merge.bed'
    #Get full path to motif database for tomtom (must be in files folder)
    tomtomdir = Functions.parent_dir(homedir) + '/files/HOCOMOCOv9_AD_MEME.txt'
    if boolean == True:
        print "Cleaning directory..."
        #Deletes all files and folders in given directory/TF/peak_files
        cl.run(directory)
    print "running main\npreparing files for MEME..."
    #Bedtools intersect on all *.bed* files , then bedtools merge to ensure non-overlapping intervals
    rc.run(directory)
    #Converts ConsolidatedPeak.merge.bed to ConsolidatedPeak.merge.fasta
    b2f.run(directory, referencefilepath)
    print "done\nrunning MEME..."
    #Runs MEME, FIMO, and TOMTOM on all ConsolidatedPeak.merge.fasta
    meme.run(directory, 10000000, 10000000, tomtomdir)
    print "done\nfixing FIMO files..."
    #Removes duplicates, orders, and eliminates first column of FIMO output files
    ff.run(directory)
    print "done\ngetting motif distances to i..."
    #Calculates motif distance to bidir center for each motif of each TF
    dist.run(directory, bidirectionalfilepath, homedir)
    print "done\ngenerating overlap numbers..."
    #Determines site overlap between bidir, ChIP, and FIMO sites
    so.run(directory, bidirectionalfilepath, homedir)
    print "done"
    