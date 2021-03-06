__author__ = 'Jonathan Rubin'

import os
import Functions
import math

def run(directory, bidirectionalfilepath, homedir):
    directorylist = Functions.fimo_directories(directory)
    
        
            
                


if __name__ == "__main__":
    #Runs on HOCOMOCO database directory
    
    
    directory = "/Users/joru1876/HOCOMOCODatabaseFIMO/FIMO_OUT"
    bidirectionalfilepath = "/Users/joru1876/ENCODEBidirectional/bidirectional_hits.merge.bed"
    homedir = "/Users/joru1876/BidirectionalTFAnalyzer/src"
    directorylist = ["/Users/joru1876/HOCOMOCODatabaseFIMO/FIMO_OUT/" + item for item in os.listdir(directory) if 'fimo_out' in item]
    distances = dict()
    for item in directorylist:
        TF = item.split('/')[5].split('_')[0]
        distances[TF] = []
    for item in directorylist:
        print item
        os.chdir(item)
        TF = item.split('/')[5].split('_')[0]
        Functions.cut_file('fimo.txt', [1,2,3], Functions.get_mod_filename('fimo.txt', 'cut'))
        distances[TF].append(Functions.get_distances_pad(bidirectionalfilepath, False, "fimo.cut.txt", True, 1500))
                
    os.chdir(homedir)
    os.chdir('..')
    os.chdir("files")
    outfile = open("TFMotifToBidirDistancePadDatabase.txt",'w')
    for key in distances:
        outfile.write(key)
        outfile.write("\n")
        for item in distances[key]: 
            if 'fimo_out' in item:   
                outfile.write(str(item))
            else:
                for value in item:
                    outfile.write(str(value))
                    outfile.write(",")
            outfile.write("\n")