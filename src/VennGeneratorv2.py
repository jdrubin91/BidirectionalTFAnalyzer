__author__ = "Jonathan Rubin"

import matplotlib
matplotlib.use('Agg')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt
import os

def run(bidirfile, chipfile, fimofile, outdir,dnasefile):
    os.system("bedtools intersect -a " + chipfile + " -b " + bidirfile + " -c > " + outdir + "/chipbidirintersect.bed")
    os.system("bedtools intersect -a " + chipfile + " -b " + fimofile + " -c > " + outdir + "/chipfimointersect.bed")
    os.system("bedtools intersect -a " + bidirfile + " -b " + fimofile + " -c > " + outdir + "/bidirfimointersect.bed")
    os.system("bedtools intersect -a " + bidirfile + " -b " + chipfile + " -c > " + outdir + "/bidirchipintersect.bed")
    os.system("bedtools intersect -a " + fimofile + " -b " + chipfile + " -c > " + outdir + "/fimochipintersect.bed")
    os.system("bedtools intersect -a " + fimofile + " -b " + bidirfile + " -c > " + outdir + "/fimobidirintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/chipbidirintersect.bed" + " -b " + fimofile + " -c > " + outdir + "/chipbidirfimointersect.bed")
    os.system("bedtools intersect -a " + outdir + "/bidirfimointersect.bed" + " -b " + chipfile + " -c > " + outdir + "/bidirfimochipintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/fimochipintersect.bed" + " -b " + bidirfile + " -c > " + outdir + "/fimochipbidirintersect.bed")
    os.system("bedtools intersect -a " + dnasefile + " -b " + chipfile + " -c > " + outdir + "/dnachipintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/dnachipintersect.bed" + " -b " + fimofile + " -c > " + outdir + "/dnachipfimointersect.bed")
    os.system("bedtools intersect -a " + outdir + "/dnachipfimointersect.bed" + " -b " + bidirfile + " -c > " + outdir + "/dnachipfimobidirintersect.bed")
    os.system("bedtools intersect -a " + chipfile + " -b " + dnasefile + " -c > " + outdir + "/chipdnaintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/chipbidirfimointersect.bed -b " + dnasefile + " -c > " + outdir + "/chipbidirfimodnaintersect.bed")

    
    chiptot = 0
    fimotot = 0
    bidirtot = 0
    dnatot = 0
    dnachip = 0
    dnafimo = 0
    dnachipfimo = 0
    dnafimobidir = 0
    dnachipfimobidir = 0 
    chipbidir = 0
    chipfimo = 0
    chipdna = 0

    
    
    bidirfimo = 0
    bidirchip = 0
    fimochip = 0
    fimobidir = 0
    chipbidirfimo = 0
    bidirfimochip = 0
    fimochipbidir = 0
    
    chipnobidir = 0
    chipnobidirfimo = 0
    chipnobidirdna = 0
    chipnobidirfimodna = 0
    
    chipnodna = 0
    chipnodnafimo = 0
    chipnodnabidir = 0
    chipnodnafimobidir = 0
    
    chipnofimo = 0
    chipnofimobidir = 0
    chipnofimodna = 0
    chipnofimobidirdna = 0
    
    chipbidirdna = 0
    chipbidirfimodna = 0
    chipfimobidir = 0
    chipfimodna = 0
    chipfimobidirdna = 0
    chipdnabidir = 0
    chipdnafimo = 0
    chipdnabidirfimo = 0
    
    with open(outdir + "/chipbidirfimodnaintersect.bed") as F0:
        for line in F0:
            dna = int(line.strip().split()[-1])
            fimo = int(line.strip().split()[-2])
            bidir = int(line.strip().split()[-3])
            if bidir != 0:
                if dna != 0:
                    chipbidirdna += 1
                    if fimo != 0:
                        chipbidirfimodna += 1
            if fimo != 0:
                if bidir != 0:
                    chipfimobidir += 1
                    if dna != 0:
                        chipfimobidirdna += 1
                if dna != 0:
                    chipfimodna += 1
            if dna != 0:
                if bidir != 0:
                    chipdnabidir += 1
                    if fimo != 0:
                        chipdnabidirfimo += 1
                if fimo != 0:
                    chipdnafimo += 1
            if fimo == 0:
                chipnofimo += 1
                if bidir != 0:
                    chipnofimobidir += 1
                    if dna != 0:
                        chipnofimobidirdna += 1
                if dna != 0:
                    chipnofimodna += 1
            if dna == 0:
                chipnodna += 1
                if fimo != 0:
                    chipnodnafimo += 1
                    if bidir != 0:
                        chipnodnafimobidir += 1
                if bidir != 0:
                    chipnodnabidir += 1
            if bidir == 0:
                chipnobidir += 1
                if fimo != 0:
                    chipnobidirfimo += 1
                    if dna != 0:
                        chipnobidirfimodna += 1
                if dna != 0:
                    chipnobidirdna += 1
    
    with open(outdir + "/chipdnaintersect.bed") as F0:
        for line in F0:
            val1 = int(line.strip().split()[-1])
            if val1 != 0:
                chipdna += 1
    
    with open(outdir + "/dnachipfimobidirintersect.bed") as F0:
        for line in F0:
            val1 = int(line.strip().split()[-1])
            val2 = int(line.strip().split()[-2])
            val3 = int(line.strip().split()[-3])
            if val2 != 0:
                dnafimo += 1
            if val3 != 0:
                dnachip += 1
            if val2 != 0 and val3 != 0:
                dnachipfimo += 1
            if val1 != 0 and val2 != 0:
                dnafimobidir += 1
            if val1 != 0 and val2 != 0 and val3 != 0:
                dnachipfimobidir += 1
            dnatot += 1
    
    with open(outdir + "/fimochipbidirintersect.bed") as F0:
        for line in F0:
            val1 = int(line.strip().split()[-1])
            val2 = int(line.strip().split()[-2])
            if val1 != 0 and val2 != 0:
                fimochipbidir += 1
    
    with open(outdir + "/bidirfimochipintersect.bed") as F0:
        for line in F0:
            val1 = int(line.strip().split()[-1])
            val2 = int(line.strip().split()[-2])
            if val1 != 0 and val2 != 0:
                bidirfimochip += 1
    
    with open(outdir + "/chipbidirfimointersect.bed") as F0:
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
            if val != 0:
                bidirfimo += 1
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
            
    
    #print "chipfile:\tchiptotal\tbidirtotal\tfimototal\tchipbidir\tchipfimo\tbidirchip\tbidirfimo\tfimochip\tfimobidir\tchipbidirfimo"
    #print chipfile,chiptot,bidirtot,fimotot,chipbidir,chipfimo,bidirchip,bidirfimo,fimochip,fimobidir,chipbidirfimo
    return chiptot, chipbidir, chipfimo, chipbidirfimo, bidirfimo, bidirfimochip, fimochip, fimotot, fimochipbidir,bidirchip, bidirtot,dnachip,dnafimo,dnatot,dnachipfimobidir,dnachipfimo,dnafimobidir,chipdna,chipnobidir, chipnobidirfimo, chipnobidirdna, chipnobidirfimodna, chipnodna, chipnodnafimo, chipnodnabidir, chipnodnafimobidir, chipnofimo, chipnofimobidir, chipnofimodna, chipnofimobidirdna,chipbidirdna, chipbidirfimodna, chipfimobidir, chipfimodna, chipfimobidirdna, chipdnabidir, chipdnafimo, chipdnabidirfimo
    
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
    bidirfile = '/scratch/Shares/dowell/ENCODE/DMSO2_3-2_divergent_classifications.bed'
    chipdir = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    fimodir = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_OUT_v10'
    dnasefile = '/scratch/Shares/dowell/ENCODE/wgEncodeUwDnaseHct116PkRep1.narrowPeak.fixed.bed'
    
    #fix_database(fimodir)
    
    list1 = [[],[]]
    list2 = [[],[]]
    list3 = [[],[],[],[],[],[]]
    list4 = [[],[],[],[]]
    list5 = [[],[],[],[]]
    list6 = [[],[],[],[]]
    list7 = [[],[],[],[]]
    list8 = [[],[],[],[]]
    list9 = [[],[],[],[]]
    for TF in os.listdir(chipdir):
        if os.path.exists(chipdir + '/' + TF + '/peak_files'):
            print TF
            if len([i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'bed' in i]) != 0:
                chipfile = chipdir + '/' + TF + '/peak_files/' + [i for i in os.listdir(chipdir + '/' + TF + '/peak_files') if 'bed' in i][0]
                for fimoTF in os.listdir(fimodir):
                    if TF == fimoTF.split('_')[0]:
                        print fimoTF
                        fimofile = fimodir + '/' + fimoTF + '/fimo.bed'
                        chiptot, chipbidir, chipfimo, chipbidirfimo,bidirfimo,bidirfimochip,fimochip,fimotot,fimochipbidir,bidirchip, bidirtot,dnachip,dnafimo,dnatot,dnachipfimobidir,dnachipfimo,dnafimobidir,chipdna,chipnobidir, chipnobidirfimo, chipnobidirdna, chipnobidirfimodna, chipnodna, chipnodnafimo, chipnodnabidir, chipnodnafimobidir, chipnofimo, chipnofimobidir, chipnofimodna, chipnofimobidirdna, chipbidirdna, chipbidirfimodna, chipfimobidir, chipfimodna, chipfimobidirdna, chipdnabidir, chipdnafimo, chipdnabidirfimo = run(bidirfile,chipfile,fimofile,chipdir + '/' + TF,dnasefile)
                        chiptot = float(chiptot)
                        chipbidir = float(chipbidir)
                        chipfimo = float(chipfimo)
                        chipbidirfimo = float(chipbidirfimo)
                        bidirfimo = float(bidirfimo)
                        bidirfimochip = float(bidirfimochip)
                        fimochip = float(fimochip)
                        fimotot = float(fimotot)
                        fimochipbidir = float(fimochipbidir)
                        bidirchip = float(bidirchip)
                        bidirtot = float(bidirtot)
                        dnachip = float(dnachip)
                        dnafimo = float(dnafimo)
                        dnatot = float(dnatot)
                        print str(dnachip/dnatot)
                        dnachipfimo = float(dnachipfimo)
                        dnafimobidir = float(dnafimobidir)
                        dnachipfimobidir = float(dnachipfimobidir)
                        chipdna = float(chipdna)
                        chipnobidir = float(chipnobidir)
                        chipnobidirfimo = float(chipnobidirfimo)
                        chipnobidirdna = float(chipnobidirdna)
                        chipnobidirfimodna = float(chipnobidirfimodna)
                        chipnodna = float(chipnodna)
                        chipnodnafimo = float(chipnodnafimo)
                        chipnodnabidir = float(chipnodnabidir)
                        chipnodnafimobidir = float(chipnodnafimobidir)
                        chipnofimo = float(chipnofimo)
                        chipnofimobidir = float(chipnofimobidir)
                        chipnofimodna = float(chipnofimodna)
                        chipnofimobidirdna = float(chipnofimobidirdna)
                        chipbidirdna = float(chipbidirdna)
                        chipbidirfimodna = float(chipbidirfimodna)
                        chipfimobidir = float(chipfimobidir)
                        chipfimodna = float(chipfimodna)
                        chipfimobidirdna = float(chipfimobidirdna)
                        chipdnabidir = float(chipdnabidir)
                        chipdnafimo = float(chipdnafimo)
                        chipdnabidirfimo = float(chipdnabidirfimo)

                        
                        list1[0].append(chipbidir/chiptot)
                        list1[1].append(chipbidirfimo/chipfimo)
                        
                        list2[0].append(chipfimo/chiptot)
                        list2[1].append(chipbidirfimo/chipbidir)
                        
                        list3[0].append(fimochip/fimotot)
                        list3[1].append(dnachip/dnatot)
                        list3[2].append(bidirchip/bidirtot)
                        list3[3].append(bidirfimochip/bidirfimo)
                        list3[4].append(dnachipfimo/dnafimo)
                        list3[5].append(dnachipfimobidir/dnafimobidir)
                        
                        list4[0].append(chipnobidir/chiptot)
                        list4[1].append(chipnobidirfimo/chipnobidir)
                        list4[2].append(chipnobidirdna/chipnobidir)
                        list4[3].append(chipnobidirfimodna/chipnobidir)
                        
                        list5[0].append(chipnodna/chiptot)
                        list5[1].append(chipnodnafimo/chipnodna)
                        list5[2].append(chipnodnabidir/chipnodna)
                        list5[3].append(chipnodnafimobidir/chipnodna)
                        
                        list6[0].append(chipnofimo/chiptot)
                        list6[1].append(chipnofimobidir/chipnofimo)
                        list6[2].append(chipnofimodna/chipnofimo)
                        list6[3].append(chipnofimobidirdna/chipnofimo)
                        
                        list7[0].append(chipbidir/chiptot)
                        list7[1].append(chipbidirfimo/chipbidir)
                        list7[2].append(chipbidirdna/chipbidir)
                        list7[3].append(chipbidirfimodna/chipbidir)
                        
                        list8[0].append(chipdna/chiptot)
                        list8[1].append(chipdnafimo/chipdna)
                        list8[2].append(chipdnabidir/chipdna)
                        list8[3].append(chipdnabidirfimo/chipdna)
                        
                        list9[0].append(chipfimo/chiptot)
                        list9[1].append(chipfimobidir/chipfimo)
                        list9[2].append(chipfimodna/chipfimo)
                        list9[3].append(chipfimobidirdna/chipfimo)
                        
                        
                        
    print list1
    F = plt.figure()
    ax1 = F.add_subplot(1,1,1)
    #ax2 = F.add_subplot(1,3,2)
    #ax3 = F.add_subplot(1,3,3)
    #ax4 = F.add_subplot(1,4,4)
    #ax1.boxplot(list1)
    #ax1.set_xticklabels(['Chip-Bid/Chip','Chip-Bid-Mot/Chip-Mot'],rotation = 45, fontsize=8)
    #ax2.boxplot(list2)
    #ax2.set_xticklabels(['Chip-Mot/Chip', 'Chip-Bid-Mot/Chip-Bid'],rotation = 45, fontsize=8)
    bp1 = ax1.boxplot(list3,patch_artist=True)
    ax1.set_xticklabels(['Mot-Chip/Mot','DNAse-Chip/DNAse','Bid-Chip/Bid','Bid-Mot-Chip/Bid-Mot','DNAse-Chip-Mot/DNAse-Mot','DNAse-Chip-Mot-Bid/DNAse-Mot-Bid'],rotation = 45, fontsize=8)
    ax1.get_xaxis().tick_bottom()
    ax1.get_yaxis().tick_left()
    #bp1 = ax1.boxplot(list4,patch_artist=True)
    #ax1.set_xticklabels(['Chip-Bid*/Chip','Chip-Bid*-Mot/Chip-Bid','Chip-Bid*-DNAse/Chip-Bid*','Chip-Bid*-Mot-DNAse/Chip-Bid*'],rotation = 45, fontsize=8)
    #ax1.get_xaxis().tick_bottom()
    #ax1.get_yaxis().tick_left()
    #bp2 = ax2.boxplot(list5,patch_artist=True)
    #ax2.set_xticklabels(['Chip-DNAse*/Chip','Chip-DNAse*-Mot/Chip-DNAse*','Chip-DNAse*-Bidir/Chip-DNAse*','Chip-DNAse*-Mot-Bidir/Chip-DNAse*'],rotation = 45, fontsize=8)
    #ax2.get_xaxis().tick_bottom()
    #ax2.get_yaxis().tick_left()
    #bp3 = ax3.boxplot(list6,patch_artist=True)
    #ax3.set_xticklabels(['Chip-Mot*/Chip','Chip-Mot*-Bid/Chip-Mot*','Chip-Mot*-DNAse/Chip-Mot*','Chip-Mot*-Bidir-DNAse/Chip-Mot*'],rotation = 45, fontsize=8)
    #ax3.get_xaxis().tick_bottom()
    #ax3.get_yaxis().tick_left()
    #ax = plt.axes()
    #plt.boxplot(list1)
    #title = bidirfile.split('/')[-1]
    #plt.title(title)
    #ax.set_xticklabels(['Chip-Bid/Chip', 'Chip-Mot/Chip', 'Chip-Bid-Mot/Chip-Bid','Chip-Bid-Mot/Chip-Mot','Bid-Mot-Chip/Bid-Mot'],rotation = 90, fontsize=8)
    
    ## change outline color, fill color and linewidth of the boxes
    for box in bp1['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp1['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp1['caps']:
        cap.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the medians
    for median in bp1['medians']:
        median.set(color='#b2df8a', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp1['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    
    ### change outline color, fill color and linewidth of the boxes
    #for box in bp2['boxes']:
    #    # change outline color
    #    box.set( color='#7570b3', linewidth=2)
    #    # change fill color
    #    box.set( facecolor = '#1b9e77' )
    ### change color and linewidth of the whiskers
    #for whisker in bp2['whiskers']:
    #    whisker.set(color='#7570b3', linewidth=2)
    ### change color and linewidth of the caps
    #for cap in bp2['caps']:
    #    cap.set(color='#7570b3', linewidth=2)
    ### change color and linewidth of the medians
    #for median in bp2['medians']:
    #    median.set(color='#b2df8a', linewidth=2)
    ### change the style of fliers and their fill
    #for flier in bp2['fliers']:
    #    flier.set(marker='o', color='#e7298a', alpha=0.5)
    #    
    ### change outline color, fill color and linewidth of the boxes
    #for box in bp3['boxes']:
    #    # change outline color
    #    box.set( color='#7570b3', linewidth=2)
    #    # change fill color
    #    box.set( facecolor = '#1b9e77' )
    ### change color and linewidth of the whiskers
    #for whisker in bp3['whiskers']:
    #    whisker.set(color='#7570b3', linewidth=2)
    ### change color and linewidth of the caps
    #for cap in bp3['caps']:
    #    cap.set(color='#7570b3', linewidth=2)
    ### change color and linewidth of the medians
    #for median in bp3['medians']:
    #    median.set(color='#b2df8a', linewidth=2)
    ### change the style of fliers and their fill
    #for flier in bp3['fliers']:
    #    flier.set(marker='o', color='#e7298a', alpha=0.5)
    
    
    plt.savefig(chipdir + '/overlap_boxplot2.png')
    