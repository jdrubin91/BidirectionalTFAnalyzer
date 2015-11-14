__author__ = 'Jonathan Rubin'

import Functions
import intervals
import os


#Sizes of all chromosomes and chromosome list (ordered) to determine offset
sizes = [249250621,243199373,198022430,191154276,180915260,171115067,
        159138663,146364022,141213431,135534747,135006516,133851895,115169878,107349540,102531392,
        90354753,81195210,78077248,59128983,63025520,48129895,51304566,59373566,155270560,16569]
chromosomes = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9',
                'chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19',
                'chr20','chr21','chr22','chrY','chrX','chrM']

#====================================================================================================
#Takes in bidirectional list of intervals (with chromosome offset calculated), a fimo file, a chip file
#and a bidirectional dictionary with key = ["'chr','start','stop'"]
def run(bidirlist,fimofile,chipfile,bidirdict):

    
#====================================================================================================
#Create a dictionary for each file (bidirectional, fimo, chip), convert (chr,start,stop) to one list
#calculating chromosome offsets from lists above

                
    fimodict = Functions.create_tup_uncut_fimo2(fimofile, True)
    fimolist = list()
    for chrom in fimodict:
        if chrom in chromosomes:
            i = chromosomes.index(chrom)
            for interval in fimodict[chrom]:
                fimolist.append((int(interval[0])+sum(sizes[0:i]),int(interval[1])+sum(sizes[0:i])))
                
    chipdict = Functions.create_tup_dict(chipfile, False)
    chiplist = list()
    for chrom in chipdict:
        if chrom in chromosomes:
            i = chromosomes.index(chrom)
            for interval in chipdict[chrom]:
                chiplist.append((int(interval[0])+sum(sizes[0:i]),int(interval[1])+sum(sizes[0:i])))
#====================================================================================================
#Using intervals, compare bidirectionals with fimo sites with chip sites, populate bidirectional
#dictionary with overlapping fimo and chip sites
        
    ST = intervals.comparison(bidirlist,fimolist,chiplist)
    AB_Overlaps = ST.find_overlaps(0,1)
    ABList = list()
    FandB = ST.find_overlaps(0,1)
    FandBList = list()
    for O in AB_Overlaps:
        for interval_original in O.overlaps:
            ABList.append((interval_original.start,interval_original.stop,interval_original.INFO))
    BC_Overlaps = ST.find_overlaps(0,2)
    
    
    return bidirdict
    
if __name__ == "__main__":
    
    bidirdict = dict()
    for line in open(bidirfile):
        if not '#' in line:
            bidirdict[','.join(line.strip().split()[0:3])] = list()
    bidirlist = list()
    for key in bidirdict:
        chrom,start,stop = key.split(',')
        if chrom in chromosomes:
            i = chromosomes.index(chrom)
            bidirlist.append((int(start)+sum(sizes[0:i]),int(stop)+sum(sizes[0:i])))
    
    print 'hello'