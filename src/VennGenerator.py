__author__ = "Jonathan Rubin"

import intervals,load
import Functions
import os
import pylab

def run(bidirfile, chipfile, fimofile, labels):
    
    A = load.bed_file(bidirfile)
    B = load.bed_file(chipfile)
    C = load.bed_file(fimofile)
    
    ST = intervals.comparison(A,B,C)
    
    return ST.compute_venn(0,1,2, display = False, labels = labels)
    
    
if __name__ == "__main__":
    bidirfile = '/scratch/Shares/dowell/TFIT/Allen2014/EMG_out_files/Allen2014_DMSO2_3-1_bidirectional_hits_intervals.bed'
    chipdir = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    
    for TF in os.listdir(chipdir):
        chipfile = chipdir + '/' + TF + '/peak_files/' + [i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'ENC' in i][0]
        for fimofolder in [i for i in os.listdir(chipdir + '/' + TF + '/peak_files/outfiles/MEME') if 'fimo_out' in i and i[0].isdigit()]:
            fimofile = chipdir + '/' + TF + '/peak_files/outfiles/MEME/' + fimofolder + '/fimo.txt'
            venn = run(bidirfile,chipfile,fimofile,['Bidirectionals',TF + 'ChIP', 'motif' + fimofolder[0]])
            pylab.savefig('venn.png')