__author__ = "Jonathan Rubin"

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def run(bidirfile, chipfile, fimofile, outdir):
    #os.system("bedtools intersect -a " + chipfile + " -b " + bidirfile + " -c > " + outdir + "/chipbidirintersect.bed")
    #os.system("bedtools intersect -a " + chipfile + " -b " + fimofile + " -c > " + outdir + "/chipfimointersect.bed")
    #os.system("bedtools intersect -a " + bidirfile + " -b " + fimofile + " -c > " + outdir + "/bidirfimointersect.bed")
    #os.system("bedtools intersect -a " + bidirfile + " -b " + chipfile + " -c > " + outdir + "/bidirchipintersect.bed")
    #os.system("bedtools intersect -a " + fimofile + " -b " + chipfile + " -c > " + outdir + "/fimochipintersect.bed")
    #os.system("bedtools intersect -a " + fimofile + " -b " + bidirfile + " -c > " + outdir + "/fimobidirintersect.bed")
    #os.system("bedtools intersect -a " + outdir + "/chipbidirintersect.bed" + " -b " + fimofile + " -c > " + outdir + "/chipbidirfimointersect.bed")
    
    chiptot = 0
    fimotot = 0
    bidirtot = 0
    chipbidir = 0
    chipfimo = 0
    bidirfimo = 0
    bidirchip = 0
    fimochip = 0
    fimobidir = 0
    chipbidirfimo = 0
    
    with open(outdir + "/chipbidirintersect.bed") as F0:
        for line in F0:
            val1 = int(line.strip().split()[-1])
            val2 = int(line.strip().split()[-2])
            if val1 != 0 and val2 != 0:
                chipbidirfimo += 1
    
    with open(outdir + "/chipbidirintersect.bed") as F1:
        for line in F1:
            val = int(line.strip().split()[-1])
            if val != 0:
                chipbidir += 1
            chiptot += 1
            
    with open(outdir + "/chipfimointersect.bed") as F2:
        for line in F2:
            val = int(line.strip().split()[-1])
            if val != 0:
                chipfimo += 1
            
    with open(outdir + "/bidirfimointersect.bed") as F3:
        for line in F3:
            val = int(line.strip().split()[-1])
            bidirfimo += val
            bidirtot += 1
    
    with open(outdir + "/bidirchipintersect.bed") as F3:
        for line in F3:
            val = int(line.strip().split()[-1])
            bidirchip += val
    
    with open(outdir + "/fimochipintersect.bed") as F3:
        for line in F3:
            val = int(line.strip().split()[-1])
            fimochip += val
            fimotot += 1
    
    with open(outdir + "/fimobidirintersect.bed") as F3:
        for line in F3:
            val = int(line.strip().split()[-1])
            fimobidir += val
            
    
    print "chipfile:\tchiptotal\tbidirtotal\tfimototal\tchipbidir\tchipfimo\tbidirchip\tbidirfimo\tfimochip\tfimobidir"
    print chipfile,chiptot,bidirtot,fimotot,chipbidir,chipfimo,bidirchip,bidirfimo,fimochip,fimobidir
    return chiptot, chipbidir, chipfimo, chipbidirfimo
    
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
    
    #fix_database(fimodir)
    
    list1 = [[],[],[],[]]
    for TF in os.listdir(chipdir):
        if os.path.exists(chipdir + '/' + TF + '/peak_files'):
            print TF
            if len([i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'bed' in i]) != 0:
                chipfile = chipdir + '/' + TF + '/peak_files/' + [i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'bed' in i][0]
                for fimoTF in os.listdir(fimodir):
                    if TF == fimoTF.split('_')[0]:
                        print fimoTF
                        fimofile = fimodir + '/' + fimoTF + '/fimo.bed'
                        chiptot, chipbidir, chipfimo, chipbidirfimo = run(bidirfile,chipfile,fimofile,chipdir + '/' + TF)
                        chiptot = float(chiptot)
                        chipbidir = float(chipbidir)
                        chipfimo = float(chipfimo)
                        chipbidirfimo = float(chipbidirfimo)
                        list1[0].append(chipbidir/chiptot)
                        list1[1].append(chipfimo/chiptot)
                        list1[2].append(chipbidirfimo/chipbidir)
                        list1[3].append(chipbidirfimo/chipfimo)
    print list1
    F = plt.figure()
    plt.boxplot(list1)
    plt.savefig(chipdir + '/overlap_boxplot.png')
    