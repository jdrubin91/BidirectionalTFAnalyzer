__author__ = 'Jonathan Rubin'

import os
import Functions

##Compares overlaps between bidirectional sites, ChIP sites (peak files), and motif sites (FIMO)

def run(directory, bidirectionalfilepath, homedir):
    TFdirectorylist = Functions.chip_peak_directories(directory)
    fimodirectorylist = Functions.fimo_directories(directory)
    counts = dict()
    for item in TFdirectorylist:
        if os.path.exists(item + "/outfiles"):
            os.chdir(item + "/outfiles")
            TF = item.split('/')[5]
            counts[TF] = []
            os.system("bedtools intersect -a " + bidirectionalfilepath + " -b ConsolidatedPeaks.merge.bed -c > Bidir_Chip_Counts.bed")
    for item in fimodirectorylist:
        os.chdir(item)
        TF = item.split('/')[5]
        fimo = item.split('/')[9]
        os.system("bedtools intersect -a " + bidirectionalfilepath + " -b fimo.cut.rmdup.ord.merge.bed -c > Bidir_Motif_Counts.bed")
        os.system("bedtools intersect -a " + directory + "/" + TF + "/peak_files/outfiles/ConsolidatedPeaks.merge.bed -b fimo.cut.rmdup.ord.merge.bed -c > Chip_Motif_Counts.bed")
        

        BidirChipFile = open(directory + "/" + TF + "/peak_files/outfiles/Bidir_Chip_Counts.bed") 
        BidirMotifFile = open("Bidir_Motif_Counts.bed")
        ChipMotifFile = open("Chip_Motif_Counts.bed")
        BidirTot = Functions.line_count("Bidir_Motif_Counts.bed")
        ChipTot = Functions.line_count("Chip_Motif_Counts.bed")
        MotifTot = Functions.line_count("fimo.cut.rmdup.ord.merge.bed")
        BidirChipCount = 0
        ChipBidirCount = 0
        BidirMotifCount = 0
        MotifBidirCount = 0
        ChipMotifCount = 0
        MotifChipCount = 0
        AllCount = 0
        for line1 in BidirChipFile:
            line2 = BidirMotifFile.readline()
            x = int(line1.strip().split()[3])
            y = int(line2.strip().split()[3])
            if x != 0 and y != 0:
                AllCount += 1.0
                ChipBidirCount += x-1
                MotifBidirCount += y-1
            elif x != 0:
                BidirChipCount += 1
                ChipBidirCount += x
            elif y != 0:
                BidirMotifCount += 1
                MotifBidirCount += y
        for line3 in ChipMotifFile:
            z = int(line3.strip().split()[3])
            if z != 0:
                ChipMotifCount += 1
                MotifChipCount += z
        ChipMotifCount =  ChipMotifCount - AllCount
        MotifChipCount = MotifChipCount - AllCount
        BidirCount = BidirTot - AllCount - BidirChipCount - BidirMotifCount
        ChipCount = ChipTot - AllCount  - ChipMotifCount - ChipBidirCount
        MotifCount = MotifTot - AllCount  - MotifBidirCount - MotifChipCount
        counts[TF].append([fimo, BidirCount, ChipCount, MotifCount, BidirChipCount, BidirMotifCount, ChipMotifCount, AllCount])
                
    os.chdir(homedir)
    os.chdir('..')
    os.chdir("./files")
    outfile = open("BidirChIpMotifOverlaps.txt",'w')
    outfile.write("TF\nMotif#\nBidir\tChip\tMotif\tBC\tBM\tCM\tBCM\n")
    for key in counts:
        outfile.write(key)
        outfile.write("\n")
        for item in counts[key]:
            outfile.write(item[0])
            outfile.write("\n")
            for i in range(1,len(item)):  
                outfile.write(str(item[i]))
                outfile.write("\t")
            outfile.write("\n")

if __name__ == "__main__":
    
#DO NOT CHANGE THIS CODE: it runs the same SiteOverlap analysis for the original HCT116 directory
    def fimo_directories(rootdirectory):
        directorylist = []
        for TF in os.listdir(rootdirectory):
            if os.path.exists(rootdirectory + "/" + TF + "/peak_files/MEME"):
                os.chdir(rootdirectory + "/" + TF + "/peak_files/MEME")
                FileList = [item for item in os.listdir(os.getcwd()) if 'fimo_out' in item]
                for fimofolder in FileList:
                    directorylist.append(rootdirectory + "/" + TF + "/peak_files/MEME/" + fimofolder)
        
        return directorylist
        
    directory = '/projects/dowellLab/ENCODE/HCT116'
    bidirectionalfilepath = '/Users/joru1876/ENCODEBidirectional/bidirectional_hits.merge.shuffle.bed'
    TFdirectorylist = Functions.chip_peak_directories(directory)
    fimodirectorylist = fimo_directories(directory)
    counts = dict()
    for item in TFdirectorylist:
        os.chdir(item)
        TF = item.split('/')[5]
        counts[TF] = []
        os.system("bedtools intersect -a " + bidirectionalfilepath + " -b Consolidatedpeaks.ord.merge.bed -c > Bidir_Chip_Counts.bed")
    for item in fimodirectorylist:
        os.chdir(item)
        TF = item.split('/')[5]
        print TF
        fimo = item.split('/')[8]
        os.system("bedtools intersect -a " + bidirectionalfilepath + " -b fimo.rmdup.ord.cut.merge.bed -c > Bidir_Motif_Counts.bed")
        os.system("bedtools intersect -a " + directory + "/" + TF + "/peak_files/Consolidatedpeaks.ord.merge.bed -b fimo.rmdup.ord.cut.merge.bed -c > Chip_Motif_Counts.bed")
        

        BidirChipFile = open(directory + "/" + TF + "/peak_files/Bidir_Chip_Counts.bed") 
        BidirMotifFile = open("Bidir_Motif_Counts.bed")
        ChipMotifFile = open("Chip_Motif_Counts.bed")
        BidirTot = Functions.line_count("Bidir_Motif_Counts.bed")
        ChipTot = Functions.line_count("Chip_Motif_Counts.bed")
        MotifTot = Functions.line_count("fimo.rmdup.ord.cut.merge.bed")
        BidirChipCount = 0
        ChipBidirCount = 0
        BidirMotifCount = 0
        MotifBidirCount = 0
        ChipMotifCount = 0
        MotifChipCount = 0
        AllCount = 0
        for line1 in BidirChipFile:
            line2 = BidirMotifFile.readline()
            x = int(line1.strip().split()[3])
            y = int(line2.strip().split()[3])
            if x != 0 and y != 0:
                AllCount += 1.0
                ChipBidirCount += x-1
                MotifBidirCount += y-1
            elif x != 0:
                BidirChipCount += 1
                ChipBidirCount += x
            elif y != 0:
                BidirMotifCount += 1
                MotifBidirCount += y
        for line3 in ChipMotifFile:
            z = int(line3.strip().split()[3])
            if z != 0:
                ChipMotifCount += 1
                MotifChipCount += z
        ChipMotifCount =  ChipMotifCount - AllCount
        MotifChipCount = MotifChipCount - AllCount
        BidirCount = BidirTot - AllCount - BidirChipCount - BidirMotifCount
        ChipCount = ChipTot - AllCount  - ChipMotifCount - ChipBidirCount
        MotifCount = MotifTot - AllCount  - MotifBidirCount - MotifChipCount
        counts[TF].append([fimo, BidirCount, ChipCount, MotifCount, BidirChipCount, BidirMotifCount, ChipMotifCount, AllCount])
                
    os.chdir('/Users/joru1876')
    #os.chdir('..')
    #os.chdir("./files")
    outfile = open("BidirChIpMotifOverlaps.shuffle.txt",'w')
    outfile.write("TF\nMotif#\nBidir\tChip\tMotif\tBC\tBM\tCM\tBCM\n")
    for key in counts:
        outfile.write(key)
        outfile.write("\n")
        for item in counts[key]:
            outfile.write(item[0])
            outfile.write("\n")
            for i in range(1,len(item)):  
                outfile.write(str(item[i]))
                outfile.write("\t")
            outfile.write("\n")