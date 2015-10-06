__author__ = 'Jonathan Rubin'

import os
import Functions
import math

def run(directory, bidirectionalfilepath, homedir):
    directorylist = Functions.fimo_directories(directory)
    
        
            
                


if __name__ == "__main__":
    #Runs on original HCT116 directory
    
    def fimo_directories(rootdirectory):
        directorylist = []
        for TF in os.listdir(rootdirectory):
            if os.path.exists(rootdirectory + "/" + TF + "/peak_files/MEME"):
                os.chdir(rootdirectory + "/" + TF + "/peak_files/MEME")
                FileList = [item for item in os.listdir(os.getcwd()) if 'fimo_out' in item]
                for fimofolder in FileList:
                    directorylist.append(rootdirectory + "/" + TF + "/peak_files/MEME/" + fimofolder)
        
        return directorylist
    
    directory = "/projects/dowellLab/ENCODE/HCT116"
    bidirectionalfilepath = "/Users/joru1876/ENCODEBidirectional/bidirectional_hits.merge.bed"
    homedir = "/Users/joru1876/BidirectionalTFAnalyzer/src"
    directorylist = fimo_directories(directory)
    distances = dict()
    for item in directorylist:
        TF = item.split('/')[5]
        distances[TF] = []
    for item in directorylist:
        print item
        os.chdir(item)
        TF = item.split('/')[5]
        Motif = item.split('/')[8]
        distances[TF].append(Motif)
        distances[TF].append(Functions.get_distances_pad(bidirectionalfilepath, False, "fimo.rmdup.ord.cut.merge.bed", True, 1500))
                
    os.chdir(homedir)
    os.chdir('..')
    os.chdir("files")
    outfile = open("TFMotifToBidirDistancePad.txt",'w')
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