__author__ = 'Jonathan Rubin'

import os
import Functions
import intervals

def run(BidirFile, ChipFile, FimoFile):
    #Give cutoff to i for motif calling
    motiftoicutoff = 100
    #Give size of window to look at ChIP reads
    windowsize = 100
    
    
    BidirDict = Functions.create_tup_bidir(BidirFile)
    ChipDict = Functions.create_bedgraph_dict(ChipFile, False)
    FimoDict = Functions.create_tup_uncut_fimo2(FimoFile, True)
    RandomizedDict = Functions.create_randomized_sites(windowsize)
    
    #Calculate reads over background by generating equally spaced random sites that are 
    #2xwindowsize in length
    #background = 0
    #genomesize = 3234830000
    BackgroundDict = dict()
    for chrom in RandomizedDict:
        if chrom in ChipDict:
            RandomList = RandomizedDict[chrom]
            ChipList = ChipDict[chrom]
            BackgroundDict[chrom] = list()
            STBackground = intervals.comparison((RandomList,ChipList))
            for O in STBackground.find_overlaps(0,1):
                for interval_original in O.overlaps:
                        if not interval_original.INFO == '':
                            BackgroundDict[chrom].append(interval_original.INFO)
    
    #Bulk of code. Will populate dictionaries (key = chrom) with ChIP coverage
    #for motif sites not in bidirectionals (as defined by motifcutoff) and for 
    #motif sites overlapping bidir calls (within motifcutoff distance)
    FnoBDict = dict()
    FandBDict = dict()
    for chrom in FimoDict:
        if chrom in BidirDict:
            if chrom in ChipDict:
                FnoBDict[chrom] = list()
                FandBDict[chrom] = list()
                BidirSites = BidirDict[chrom]
                
                #Apply motif distance to i cutoff to bidirectional sites (i.e.
                #collapse bidirectional sites into cutoff window)
                BidirPaddedSites = list()
                for site in BidirSites:
                    mid = (site[0]+site[1])/2
                    start = mid-motiftoicutoff
                    stop = mid+motiftoicutoff
                    BidirPaddedSites.append((start,stop))
                    
                ChipSites = ChipDict[chrom]
                FimoSites = FimoDict[chrom]
                
                #Create interval tree between padded Bidir sites and FIMO motif
                #sites.  Compares motif sites that are at cutoff distance to 
                #bidir site.
                ST1 = intervals.comparison((BidirPaddedSites,FimoSites))
                FnoB = ST1.get_isolated(1)
                
                #Find motifs that do not overlap a bidirectional, expand sites
                #to mid+-windowsize
                FnoBList = list()
                for I in FnoB:
                    mid = (I.start+I.stop)/2
                    FnoBList.append((mid-windowsize,mid+windowsize))
                
                #Find motifs that overlap a bidirectional, expand sites to 
                #mid+-windowsize
                FandB = ST1.find_overlaps(0,1)
                FandBList = list()
                for O in FandB:
                    for interval_original in O.overlaps:
                        if not interval_original.INFO == '':
                            mid = (interval_original.start+interval_original.stop)/2
                            FandBList.append((mid-windowsize,mid+windowsize))
                            
                
                #Find ChIP coverage over motif sites that do not overlap a bidir
                ST2 = intervals.comparison(FnoBList, ChipSites)
                FnoBChipOverlaps = ST2.find_overlaps(0,1)
                #FnoBtotalsize = 0
                for O in FnoBChipOverlaps:
                    for interval_original in O.overlaps:
                        if not interval_original.INFO == '':
                            FnoBDict[chrom].append(interval_original.INFO)
                            #FnoBtotalsize += interval_original.stop - interval_original.start
                    
                
                #Find ChIP coverage over motif sites that overlap a bidir
                ST3 = intervals.comparison(FandBList,ChipSites)
                FandBChipOverlaps = ST3.find_overlaps(0,1)
                #FandBtotalsize = 0
                for O in FandBChipOverlaps:
                    for interval_original in O.overlaps:
                        if not interval_original.INFO == '':
                            FandBDict[chrom].append(interval_original.INFO)
                            #FandBtotalsize += interval_original.stop - interval_original.start
                
            
    
    return BackgroundDict, FnoBDict, FandBDict
    
    
if __name__ == "__main__":
    #Specify paths to directories or files
    BidirFile = '/scratch/Users/joru1876/Allen2014_DMSO2_3-1_bidirectional_hits_intervals.bed'
    ChipDir = '/scratch/Users/joru1876/HCT116v2'
    FimoDir = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO'
    
    FIMOTFDict = dict()
    for TF in Functions.HOCOMOCO_fimo_directories(FimoDir):
        TFlist = TF.split('/')
        FIMOTFDict[TFlist[len(TFlist)-1][0:TFlist[len(TFlist)-1].index('_')]] = TF
    
    ChipDirList = Functions.chip_bedgraph_directories(ChipDir)
    for directory in ChipDirList:
        print Functions.parent_dir(directory) + '/ChIPMotifValidator_out'
        directorylist = directory.split('/')
        TF = directorylist[len(directorylist)-2]
        if TF in FIMOTFDict:
	    print TF
            ChipFile = directory + '/' + [i for i in os.listdir(directory) if 'ENC' in i][0]
            BackgroundDict, FnoBDict, FandBDict = run(BidirFile,ChipFile,FIMOTFDict[TF] + '/fimo.txt')
            
            if not os.path.exists(Functions.parent_dir(directory) + '/ChIPMotifValidator_out'):
                os.mkdir(Functions.parent_dir(directory) + '/ChIPMotifValidator_out')
            os.chdir(Functions.parent_dir(directory) + '/ChIPMotifValidator_out')
            outfile1 = open('Background100.txt','w')
            for chrom in BackgroundDict:
                outfile1.write(chrom)
                outfile1.write('\t')
                outfile1.write(BackgroundDict[chrom])
                outfile1.write('\n')
            outfile2 = open('FnoB100.txt','w')
            for chrom in FnoBDict:
                outfile2.write(chrom)
                outfile2.write('\t')
                outfile2.write(FnoBDict[chrom])
                outfile2.write('\n')
            outfile3 = open('FandB100.txt','w')
            for chrom in FandBDict:
                outfile3.write(chrom)
                outfile3.write('\t')
                outfile3.write(FandBDict[chrom])
                outfile3.write('\n')
