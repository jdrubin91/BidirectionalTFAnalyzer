__author__ = "Jonathan Rubin"

import intervals,load
import Functions

def run(bidirfile, chipfile, fimofile, labels):
    
    A = load.bed_file(bidirfile)
    B = load.bed_file(chipfile)
    C = load.bed_file(fimofile)
    
    ST = intervals.comparison(A,B,C)
    
    return ST.compute_venn(0,1,2, display = False, labels = labels)
    
    
if __name__ == "__main__":
    bidirfile = 'path to bidirectional file'
    chipfilelist = Functions.chip_peak_directories('path to HCT116')
    
    