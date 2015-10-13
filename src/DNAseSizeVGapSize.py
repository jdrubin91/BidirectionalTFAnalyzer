__author__ = 'Jonathan Rubin'

import os
import node
import Functions

#R

def run(bidirectionalfile, DNAseFile):
    bidirlist = Functions.parse_bidirfile(bidirectionalfile)
    bidirdict = dict()
    datapoints = []
    for item in bidirlist:
        chrom, start, stop, parameters = item
        if chrom not in bidirdict:
            bidirdict[chrom] = []
        else:
            bidirdict[chrom].append((start,stop,parameters))
    
    dnasedict = Functions.create_tup_dict(DNAseFile, False)
    for chrom in dnasedict:
        if chrom in bidirdict:
            bidirtree = node.tree(bidirdict[chrom])
            for item in dnasedict[chrom]:
                bidirsite = bidirtree.searchInterval(item)
                if len(bidirsite) != 0:
                    start = float(item[0])
                    stop = float(item[1])
                    size = stop - start
                    datapoints.append((bidirsite[2][6],size))
                    
    return datapoints
                    
                    
                    
if __name__ == "__main__":
    dnasefile = '/projects/dowellLab/ENCODE/HCT116/DNAse/peak_files/'
            
            