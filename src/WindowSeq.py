__author__ = 'Jonathan Rubin'

import Functions
import os

def run(bidirfile,windowsize):
    #Takes in a bidirectional file and outputs a dictionary of {chrom: [(start,stop)]}
    #based on windowsize
    bidirdict = dict()
    bidirlist = Functions.parse_bidirfile(bidirfile)
    for item in bidirlist:
        chrom,start,stop = item[0:3]
        if not chrom in bidirdict:
            bidirdict[chrom] = list()
        mid = (float(start)+float(stop))/2
        bidirdict[chrom].append((int(mid-windowsize),int(mid+windowsize)))
    
    return bidirdict
    
if __name__ == "__main__":
    ##Returns fasta file with sequences within windowsize of i
    #Specify windowsize:
    windowsize = 6
    #Specify TFIT directory
    TFIT = '/scratch/Shares/dowell/TFIT'
    #Specify reference fasta file
    referencefilepath = '/scratch/Shares/dowell/pubgro/genomefiles/human/hg19/hg19ucsc/hg19_all.fa'
    
    for directory in Functions.TFIT_EMG_OUT_directories(TFIT):
        for bidirfile in os.listdir(directory):
            if 'bed' in bidirfile:
                print bidirfile
                bidirdict = run(directory + '/' + bidirfile, windowsize)
                if not os.path.exists(Functions.parent_dir(directory) + '/WindowSeq_out'):
                    os.mkdir(Functions.parent_dir(directory) + '/WindowSeq_out')
                os.chdir(Functions.parent_dir(directory) + '/WindowSeq_out')
                outfile = open(bidirfile[0:bidirfile.index('.')] + '.wseq.bed','w')
                for chrom in bidirdict:
                    for tup in bidirdict[chrom]:
                        start, stop = tup
                        outfile.write(chrom)
                        outfile.write('\t')
                        outfile.write(str(start))
                        outfile.write('\t')
                        outfile.write(str(stop))
                        outfile.write('\n')
                os.system("bedtools getfasta -fi " + referencefilepath + " -bed " + bidirfile[0:bidirfile.index('.')] + ".wseq.bed -fo " + bidirfile[0:bidirfile.index('.')] + '.wseq.fasta')