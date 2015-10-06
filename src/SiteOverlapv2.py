__author__ = 'Jonathan Rubin'

import os
import Functions

def run(directory, bidirectionalfilepath, homedir):
    fimodirectorylist = Functions.fimo_directories(directory)
    counts = dict()
    for fimo in fimodirectorylist:
        TF = fimo.split('/')[5]
        if TF not in counts:
            counts[TF] = []
        fimoname = fimo.split('/')[9]
        fimofile = fimo + "/fimo.cut.rmdup.ord.merge.bed"
        chipfile = Functions.parent_dir(Functions.parent_dir(fimo)) + '/ConsolidatedPeaks.merge.bed'
        vennlist = Functions.venn_d3(bidirectionalfilepath, chipfile, fimofile) 
        counts[TF].append([fimoname, vennlist])
    
    os.chdir(homedir)
    os.chdir('..')
    os.chdir("./files")
    outfile = open("BidirChIpMotifOverlaps.txt",'w')
    outfile.write("TF\nMotif#\nBidir\tChip\tMotif\tBC\tCB\tBM\tMB\tCM\tMC\tBCM\tCBM\tMBC\n")
    for key in counts:
        outfile.write(key)
        outfile.write("\n")
        for item in counts[key]:
            outfile.write(item[0])
            outfile.write("\n")
            for value in item[1]:  
                outfile.write(value)
                outfile.write("\t")
            outfile.write("\n")
            

if __name__ == "__main__":
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
    bidirectionalfilepath = '/Users/joru1876/ENCODEBidirectional/bidirectional_hits.merge.bed'
    homedir = '/Users/joru1876/test'
    fimodirectorylist = fimo_directories(directory)
    counts = dict()
    for fimo in fimodirectorylist:
        if os.path.exists(Functions.parent_dir(Functions.parent_dir(fimo)) + '/Consolidatedpeaks.ord.merge.bed'):
            TF = fimo.split('/')[5]
            if TF not in counts:
                counts[TF] = []
            fimoname = fimo.split('/')[8]
            fimofile = fimo + "/fimo.rmdup.ord.cut.merge.bed"
            chipfile = Functions.parent_dir(Functions.parent_dir(fimo)) + '/Consolidatedpeaks.ord.merge.bed'
            vennlist = Functions.venn_d3(bidirectionalfilepath, False, chipfile, False, fimofile, True) 
            counts[TF].append([fimoname, vennlist])
    
    os.chdir(homedir)
    outfile = open("BidirChIpMotifOverlaps.txt",'w')
    outfile.write("TF\nMotif#\nBidir\tChip\tMotif\tBC\tCB\tBM\tMB\tCM\tMC\tBCM\tCBM\tMBC\n")
    for key in counts:
        outfile.write(key)
        outfile.write("\n")
        for item in counts[key]:
            outfile.write(item[0])
            outfile.write("\n")
            for value in item[1]:  
                outfile.write(str(value))
                outfile.write("\t")
            outfile.write("\n")