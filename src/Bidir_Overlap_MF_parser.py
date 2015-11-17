__author__ = 'Jonathan Rubin'

import Functions
import os

if __name__ == "__main__":
    bidirfile = open('C:\cygwin64\home\Jonathan\Master_Files\Allen2014_overlaps.bed')
    
    line = bidirfile.readline()
    print line
    
    #fimocount = 0
    #bidircount = 0
    #chipcount = 0
    #for line in bidirfile:
    #    overlaps = line.strip().split('|')[1].split(',')
    #    for item in overlaps:
    #        if 'fimo_out' in item:
    #            fimocount += 1
    #        else:
    #            chipcount += 1
