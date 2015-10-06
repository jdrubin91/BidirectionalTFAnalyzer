__author__ = 'Jonathan Rubin'

##Calculates distance of center of motif to center of bidirectional site

import os
import Functions
import math
import numpy as np

def run(directory, bidirectionalfilepath, homedir):
    directorylist = Functions.fimo_directories(directory)
    distances = dict()
    for item in directorylist:
        if os.path.exists(item):
            os.chdir(item)
            TF = item.split('/')[5]
            Motif = item.split('/')[9]
            os.system("bedtools intersect -a " + bidirectionalfilepath + " -b fimo.cut.rmdup.ord.merge.bed -wa -wb > BidirectionalMotifIntersect.bed")
            FileList = Functions.parse_file("BidirectionalMotifIntersect.bed")
            fimodist = []
            for line in FileList:
                chrom1, start1, stop1, chrom2, start2, stop2 = line[0:6]
                i = (float(start1) + float(stop1))/2
                x = (float(start2) + float(stop2))/2
                fimodist.append((i-x)/(float(stop1)-float(start1)))
            if len(fimodist) > 0:
                if TF in distances:
                    distances[TF].append(Motif)
                    distances[TF].append(fimodist)
                else:
                    distances[TF] = [Motif, fimodist]
                
    os.chdir(homedir)
    os.chdir('..')
    os.chdir("./files")
    outfile = open("TFMotifToBidirDistance.txt",'w')
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
    
    
if __name__ == "__main__":
    #DO NOT CHANGE THIS CODE: it runs MotifDistance on original HCT116 directory
    
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
        os.chdir(item)
        TF = item.split('/')[5]
        Motif = item.split('/')[8]
        os.system("bedtools intersect -a " + bidirectionalfilepath + " -b fimo.rmdup.ord.cut.merge.bed -wa -wb > BidirectionalMotifIntersect.bed")
        FileList = Functions.parse_file("BidirectionalMotifIntersect.bed")
        fimodist = []
        for line in FileList:
            chrom1, start1, stop1, chrom2, start2, stop2 = line[0:6]
            i = (float(start1) + float(stop1))/2
            x = (float(start2) + float(stop2))/2
            fimodist.append((i-x)/((float(stop1)-float(start1))/2))
        if len(fimodist) > 0:
            if TF in distances:
                samplemean = np.mean(fimodist)
                samplestanddev = np.std(fimodist)
                z = samplemean/(samplestanddev/math.sqrt(len(fimodist)))
                distances[TF].append(Motif)
                distances[TF].append(fimodist)
            else:
                distances[TF] = [Motif, fimodist]
                
    os.chdir(homedir)
    os.chdir('..')
    os.chdir("files")
    outfile = open("TFMotifToBidirDistance.txt",'w')
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