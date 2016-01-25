__author__ = "Jonathan Rubin"

import matplotlib
matplotlib.use('Agg')
import intervals
import Functions
import os
import pylab

def run(bidirfile, chipfile, fimofile, labels):
    
    sizes = [249250621,243199373,198022430,191154276,180915260,171115067,
            159138663,146364022,141213431,135534747,135006516,133851895,115169878,107349540,102531392,
            90354753,81195210,78077248,59128983,63025520,48129895,51304566,59373566,155270560,16569]
    chromosomes = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9',
                    'chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19',
                    'chr20','chr21','chr22','chrY','chrX','chrM']
    
    A = Functions.create_dictv2(bidirfile)
    Alist = list()
    for chrom in A:
        if chrom in chromosomes:
            i = chromosomes.index(chrom)
            for interval in A[chrom]:
                Alist.append((int(interval[0])+sum(sizes[0:i]),int(interval[1])+sum(sizes[0:i])))
            
    B = Functions.create_dictv2(chipfile)
    Blist = list()
    for chrom in B:
        if chrom in chromosomes:
            i = chromosomes.index(chrom)
            for interval in B[chrom]:
                Blist.append((int(interval[0])+sum(sizes[0:i]),int(interval[1])+sum(sizes[0:i])))
            
    C = Functions.create_dictv2(fimofile)
    Clist = list()
    for chrom in C:
        if chrom in chromosomes:
            i = chromosomes.index(chrom)
            for interval in C[chrom]:
                Clist.append((int(interval[0])+sum(sizes[0:i]),int(interval[1])+sum(sizes[0:i])))
    
    ST = intervals.comparison(Alist,Blist,Clist)
    
    return ST.compute_venn(0,1,2, display = False, labels = labels)
    
    
if __name__ == "__main__":
    bidirfile = '/scratch/Shares/dowell/TFIT/Allen2014/EMG_out_files/current_predictions/Allen2014_DMSO2_3-19_divergent_classifications.bed'
    chipdir = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    
    for TF in os.listdir(chipdir):
        print TF
        if len(os.listdir(chipdir + '/' + TF + '/peak_files')) != 0:
            chipfile = chipdir + '/' + TF + '/peak_files/' + [i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'ENC' in i][0]
            for fimofolder in [i for i in os.listdir(chipdir + '/' + TF + '/peak_files/outfiles/MEME') if 'fimo_out' in i and i[0].isdigit()]:
                print fimofolder
                Functions.cut_file(chipdir + '/' + TF + '/peak_files/outfiles/MEME/' + fimofolder + '/fimo.txt',[1,2,3],chipdir + '/' + TF + '/peak_files/outfiles/MEME/' + fimofolder + '/fimo.cut.txt')
                fimofile = chipdir + '/' + TF + '/peak_files/outfiles/MEME/' + fimofolder + '/fimo.cut.txt'
                Functions.replace_header(fimofile, '#')
                venn = run(bidirfile,chipfile,fimofile,('Bidirectionals',TF + 'ChIP', 'motif' + fimofolder[0]))
                pylab.savefig('venn.png')