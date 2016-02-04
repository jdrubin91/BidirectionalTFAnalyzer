__author__ = "Jonathan Rubin"

import matplotlib
matplotlib.use('Agg')
import os

def run(bidirfile, chipfile, fimofile, outdir):
    os.system("bedtools intersect -a " + chipfile + " -b " + bidirfile + " -c > " + outdir + "/chipbidirintersect.bed")
    os.system("bedtools intersect -a " + chipfile + " -b " + fimofile + " -c > " + outdir + "/chipfimointersect.bed")
    os.system("bedtools intersect -a " + bidirfile + " -b " + fimofile + " -c > " + outdir + "/bidirfimointersect.bed")
    
    chipbidir = 0
    chipfimo = 0
    bidirfimo = 0
    
    with open(outdir + "/chipbidirintersect.bed") as F1:
        for line in F1:
            val = int(line.strip().split()[-1])
            chipbidir += val
            
    with open(outdir + "/chipfimointersect.bed") as F2:
        for line in F2:
            val = int(line.strip().split()[-1])
            chipfimo += val
            
    with open(outdir + "/bidirfimointersect.bed") as F3:
        for line in F3:
            val = int(line.strip().split()[-1])
            bidirfimo += val
            
    print chipfile,chipbidir,chipfimo,bidirfimo
    
def fix_database(directory):
    for TF in os.listdir(directory):
        file1 = directory + '/' + TF + '/fimo.cut.txt'
        outfile = open(directory + '/' + TF + '/fimo.bed','w')
        with open(file1) as F1:
            for line in F1:
                if 'chr' in line.strip().split()[0]:
                    chrom,start,stop = line.strip().split()[0:3]
                    outfile.write(chrom + '\t' + start + '\t' + stop + '\n')
        outfile.close()
    
if __name__ == "__main__":
    bidirfile = '/scratch/Shares/dowell/TFIT/Allen2014/EMG_out_files/current_predictions/Allen2014_DMSO2_3-19_divergent_classifications.bed'
    chipdir = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    fimodir = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_OUT_v10'
    
    fix_database(fimodir)
    
    #for TF in os.listdir(chipdir):
    #    print TF
    #    if len([i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'bed' in i]) != 0:
    #        chipfile = chipdir + '/' + TF + '/peak_files/' + [i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'bed' in i][0]
    #        for fimoTF in os.listdir(fimodir):
    #            if TF == fimoTF.split('_')[0]:
    #                print fimoTF
    #                fimofile = fimodir + '/' + fimoTF + '/fimo.bed'
    #                run(bidirfile,chipfile,fimofile,chipdir + '/' + TF)