__author__ = "Jonathan Rubin"

import matplotlib
matplotlib.use('Agg')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt
from scipy import stats
import os

directory = '/scratch/Shares/dowell/ENCODE/TF_CT'
fimodir = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_OUT_v10'
imagedir = '/scratch/Users/joru1876/BidirectionalTFAnalyzer/images'

def run(bidirfile, chipfile, fimofile, outdir,dnasefile):
    os.system("bedtools intersect -a " + chipfile + " -b " + bidirfile + " -c > " + outdir + "/chipbidirintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/chipbidirintersect.bed" + " -b " + fimofile + " -c > " + outdir + "/chipbidirfimointersect.bed")
    os.system("bedtools intersect -a " + outdir + "/chipbidirfimointersect.bed -b " + dnasefile + " -c > " + outdir + "/chipbidirfimodnaintersect.bed")
    os.system("bedtools intersect -a " + bidirfile + " -b " + fimofile + " -c > " + outdir + "/bidirfimointersect.bed")
    os.system("bedtools intersect -a " + fimofile + " -b " + chipfile + " -c > " + outdir + "/fimochipintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/bidirfimointersect.bed" + " -b " + chipfile + " -c > " + outdir + "/bidirfimochipintersect.bed")
    os.system("bedtools intersect -a " + dnasefile + " -b " + chipfile + " -c > " + outdir + "/dnachipintersect.bed")
    os.system("bedtools intersect -a " + outdir + "/dnachipintersect.bed" + " -b " + fimofile + " -c > " + outdir + "/dnachipfimointersect.bed")
    os.system("bedtools intersect -a " + outdir + "/dnachipfimointersect.bed" + " -b " + bidirfile + " -c > " + outdir + "/dnachipfimobidirintersect.bed")
    
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
    bidirchip = 0
    fimochip = 0
    chipbidirfimo = 0
    bidirfimochip = 0
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
    bidirfimo = 0
    
    with open(fimofile) as F:
        for line in F:
            fimotot += 1.0
    
    with open(outdir + "/dnachipintersect.bed") as F:
        for line in F:
            chip = int(line.strip().split()[-1])
            if chip != 0:
                fimochip += 1.0
                
    with open(outdir + "/bidirfimochipintersect.bed") as F:
        for line in F:
            chip = int(line.strip().split()[-1])
            fimo = int(line.strip().split()[-2])
            bidirtot += 1.0
            if chip != 0:
                bidirchip += 1.0
                if fimo != 0:
                    bidirfimochip += 1.0
            if fimo != 0:
                bidirfimo += 1.0
    
    with open(outdir + "/dnachipfimobidirintersect.bed") as F:
        for line in F:
            bidir = int(line.strip().split()[-1])
            fimo = int(line.strip().split()[-2])
            chip = int(line.strip().split()[-3])
            dnatot += 1.0
            if chip != 0:
                dnachip += 1.0
                if fimo != 0:
                    dnachipfimo += 1.0
                    if bidir != 0:
                        dnachipfimobidir += 1.0
            if fimo != 0:
                dnafimo += 1.0
                if bidir != 0:
                    dnafimobidir += 1.0
    
    with open(outdir + "/chipbidirfimodnaintersect.bed") as F0:
        for line in F0:
            dna = int(line.strip().split()[-1])
            fimo = int(line.strip().split()[-2])
            bidir = int(line.strip().split()[-3])
            chiptot += 1.0
            if bidir != 0:
                chipbidir += 1.0
                if dna != 0:
                    chipbidirdna += 1.0
                    if fimo != 0:
                        chipbidirfimodna += 1.0
                if fimo != 0:
                    chipbidirfimo += 1.0
            if fimo != 0:
                chipfimo += 1.0
                if bidir != 0:
                    chipfimobidir += 1.0
                    if dna != 0:
                        chipfimobidirdna += 1.0
                if dna != 0:
                    chipfimodna += 1.0
            if dna != 0:
                chipdna += 1.0
                if bidir != 0:
                    chipdnabidir += 1.0
                    if fimo != 0:
                        chipdnabidirfimo += 1.0
                if fimo != 0:
                    chipdnafimo += 1.0
            if fimo == 0:
                chipnofimo += 1.0
                if bidir != 0:
                    chipnofimobidir += 1.0
                    if dna != 0:
                        chipnofimobidirdna += 1.0
                if dna != 0:
                    chipnofimodna += 1.0
            if dna == 0:
                chipnodna += 1.0
                if fimo != 0:
                    chipnodnafimo += 1.0
                    if bidir != 0:
                        chipnodnafimobidir += 1.0
                if bidir != 0:
                    chipnodnabidir += 1.0
            if bidir == 0:
                chipnobidir += 1.0
                if fimo != 0:
                    chipnobidirfimo += 1.0
                    if dna != 0:
                        chipnobidirfimodna += 1.0
                if dna != 0:
                    chipnobidirdna += 1.0
    
    
    return chiptot,fimotot,bidirtot,dnatot,dnachip,dnafimo,dnachipfimo,dnafimobidir,dnachipfimobidir,chipbidir,chipfimo,chipdna,bidirchip,fimochip,chipbidirfimo,bidirfimochip,chipnobidir,chipnobidirfimo,chipnobidirdna,chipnobidirfimodna,chipnodna,chipnodnafimo,chipnodnabidir,chipnodnafimobidir,chipnofimo,chipnofimobidir,chipnofimodna,chipnofimobidirdna,chipbidirdna,chipbidirfimodna,chipfimobidir,chipfimodna,chipfimobidirdna,chipdnabidir,chipdnafimo,chipdnabidirfimo,bidirfimo
    
def fix_directory(directory):
    for cell in os.listdir(directory):
        for chip in os.listdir(directory + '/' + cell):
            if 'ENC' in chip and not 'sorted' in chip and not 'cut' in chip:
                print chip
                outfile = open(directory + '/' + cell + '/' + chip.split('.')[0] + '.cut.bed','w')
                with open(directory + '/' + cell + '/' + chip) as F:
                    for line in F:
                        line = line.strip().split()
                        outfile.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')
                outfile.close()
                if os.path.exists(directory + '/' + cell + '/' + chip.split('.')[0] + '.cut.sorted.bed'):
                    os.system("rm " + directory + '/' + cell + '/' + chip.split('.')[0] + ".cut.sorted.bed")
                os.system("sort -k1,1 -k2,2n " + directory + '/' + cell + '/' + chip.split('.')[0] + ".cut.bed > " + directory + '/' + cell + '/' + chip.split('.')[0] + ".cut.sorted.bed")
                
    
if __name__ == "__main__":
    #fix_directory(directory)
    list3 = [[],[],[],[],[],[]]
    list4 = [[],[],[],[]]
    list5 = [[],[],[],[]]
    list6 = [[],[],[],[]]
    list7 = [[],[],[],[]]
    list8 = [[],[],[],[]]
    list9 = [[],[],[],[]]
    for cell in os.listdir(directory):
        if not 'boxplot' in cell:
            print cell
            #list3 = [[],[],[],[],[],[]]
            #list4 = [[],[],[],[]]
            #list5 = [[],[],[],[]]
            #list6 = [[],[],[],[]]
            #list7 = [[],[],[],[]]
            #list8 = [[],[],[],[]]
            #list9 = [[],[],[],[]]
            metadata = dict()
            with open(directory + '/' + cell + '/metadata.tsv') as F1:
                for line in F1:
                    if 'E' in line[0] and 'optimal'in line:
                        line = line.strip().split()
                        metadata[line[0] + '.cut.sorted.bed'] = line[18].split('-')[0]
            bidirfile = directory + '/' + cell + '/' + [chip for chip in os.listdir(directory + '/' + cell) if 'SRR' in chip][0]
            print bidirfile
            dnasefile = directory + '/' + cell + '/' + [dnase for dnase in os.listdir(directory + '/' + cell) if 'DNASE' in dnase and 'sorted' in dnase][0]
            print dnasefile
            for chip in os.listdir(directory + '/' + cell):
                if chip in metadata:
                    print chip
                    TF = metadata[chip]
                    for fimoTF in os.listdir(fimodir):
                        if TF == fimoTF.split('_')[0]:
                            print TF,fimoTF
                            fimofile = fimodir + '/' + fimoTF + '/fimo.bed'
                            chipfile = directory + '/' + cell + '/' + chip
                            outdir = directory + '/' + cell + '/temp'
                            chiptot,fimotot,bidirtot,dnatot,dnachip,dnafimo,dnachipfimo,dnafimobidir,dnachipfimobidir,chipbidir,chipfimo,chipdna,bidirchip,fimochip,chipbidirfimo,bidirfimochip,chipnobidir,chipnobidirfimo,chipnobidirdna,chipnobidirfimodna,chipnodna,chipnodnafimo,chipnodnabidir,chipnodnafimobidir,chipnofimo,chipnofimobidir,chipnofimodna,chipnofimobidirdna,chipbidirdna,chipbidirfimodna,chipfimobidir,chipfimodna,chipfimobidirdna,chipdnabidir,chipdnafimo,chipdnabidirfimo,bidirfimo = run(bidirfile, chipfile, fimofile, outdir,dnasefile)
                            
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
    
    
    print "Boxplot1:"
    for i in range(len(list3)-1):
        print stats.ks_2samp(list3[i],list3[i+1])
    print "Boxplot2:"
    for i in range(len(list4)-1):
        print stats.ks_2samp(list4[i],list4[i+1])
    for i in range(len(list5)-1):
        print stats.ks_2samp(list5[i],list5[i+1])
    for i in range(len(list6)-1):
        print stats.ks_2samp(list6[i],list6[i+1])
    print "Boxplot3:"
    for i in range(len(list7)-1):
        print stats.ks_2samp(list7[i],list7[i+1])
    for i in range(len(list8)-1):
        print stats.ks_2samp(list8[i],list8[i+1])
    for i in range(len(list9)-1):
        print stats.ks_2samp(list9[i],list9[i+1])
        
        
                            
    F = plt.figure()
    ax1 = F.add_subplot(1,1,1)
    bp1 = ax1.boxplot(list3,patch_artist=True)
    ax1.set_xticklabels(['Mot-Chip/Mot','DNAse-Chip/DNAse','Bid-Chip/Bid','Bid-Mot-Chip/Bid-Mot','DNAse-Chip-Mot/DNAse-Mot','DNAse-Chip-Mot-Bid/DNAse-Mot-Bid'],rotation = 45, fontsize=8)
    ax1.get_xaxis().tick_bottom()
    ax1.get_yaxis().tick_left()
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
    
    #plt.savefig(directory + '/' + cell + '/' + cell + '_overlap_boxplot1.png')
    plt.savefig(directory + '/' + 'All_overlap_boxplot1.svg')
    
    F1 = plt.figure()
    ax1 = F1.add_subplot(1,3,1)
    ax2 = F1.add_subplot(1,3,2)
    ax3 = F1.add_subplot(1,3,3)
    
    bp1 = ax1.boxplot(list4,patch_artist=True)
    ax1.set_xticklabels(['Chip-Bid*/Chip','Chip-Bid*-Mot/Chip-Bid*','Chip-Bid*-DNAse/Chip-Bid*','Chip-Bid*-Mot-DNAse/Chip-Bid*'],rotation = 45, fontsize=8)
    ax1.get_xaxis().tick_bottom()
    ax1.get_yaxis().tick_left()
    bp2 = ax2.boxplot(list5,patch_artist=True)
    ax2.set_xticklabels(['Chip-DNAse*/Chip','Chip-DNAse*-Mot/Chip-DNAse*','Chip-DNAse*-Bidir/Chip-DNAse*','Chip-DNAse*-Mot-Bidir/Chip-DNAse*'],rotation = 45, fontsize=8)
    ax2.get_xaxis().tick_bottom()
    ax2.get_yaxis().tick_left()
    bp3 = ax3.boxplot(list6,patch_artist=True)
    ax3.set_xticklabels(['Chip-Mot*/Chip','Chip-Mot*-Bid/Chip-Mot*','Chip-Mot*-DNAse/Chip-Mot*','Chip-Mot*-Bidir-DNAse/Chip-Mot*'],rotation = 45, fontsize=8)
    ax3.get_xaxis().tick_bottom()
    ax3.get_yaxis().tick_left()
    
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
    
    ## change outline color, fill color and linewidth of the boxes
    for box in bp2['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp2['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp2['caps']:
        cap.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the medians
    for median in bp2['medians']:
        median.set(color='#b2df8a', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp2['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
        
    ## change outline color, fill color and linewidth of the boxes
    for box in bp3['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp3['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp3['caps']:
        cap.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the medians
    for median in bp3['medians']:
        median.set(color='#b2df8a', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp3['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    
    
    #plt.savefig(directory + '/' + cell + '/' + cell + '_overlap_boxplot2.png')
    plt.savefig(directory + '/' + 'All_overlap_boxplot2.svg')
    
    
    F2 = plt.figure()
    ax1 = F2.add_subplot(1,3,1)
    ax2 = F2.add_subplot(1,3,2)
    ax3 = F2.add_subplot(1,3,3)
    
    bp1 = ax1.boxplot(list7,patch_artist=True)
    ax1.set_xticklabels(['Chip-Bid/Chip','Chip-Bid-Mot/Chip-Bid','Chip-Bid-DNAse/Chip-Bid','Chip-Bid-Mot-DNAse/Chip-Bid'],rotation = 45, fontsize=8)
    ax1.get_xaxis().tick_bottom()
    ax1.get_yaxis().tick_left()
    bp2 = ax2.boxplot(list8,patch_artist=True)
    ax2.set_xticklabels(['Chip-DNAse/Chip','Chip-DNAse-Mot/Chip-DNAse','Chip-DNAse-Bidir/Chip-DNAse','Chip-DNAse-Mot-Bidir/Chip-DNAse'],rotation = 45, fontsize=8)
    ax2.get_xaxis().tick_bottom()
    ax2.get_yaxis().tick_left()
    bp3 = ax3.boxplot(list9,patch_artist=True)
    ax3.set_xticklabels(['Chip-Mot/Chip','Chip-Mot-Bid/Chip-Mot','Chip-Mot-DNAse/Chip-Mot','Chip-Mot-Bidir-DNAse/Chip-Mot'],rotation = 45, fontsize=8)
    ax3.get_xaxis().tick_bottom()
    ax3.get_yaxis().tick_left()
    
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
    
    ## change outline color, fill color and linewidth of the boxes
    for box in bp2['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp2['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp2['caps']:
        cap.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the medians
    for median in bp2['medians']:
        median.set(color='#b2df8a', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp2['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
        
    ## change outline color, fill color and linewidth of the boxes
    for box in bp3['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp3['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp3['caps']:
        cap.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the medians
    for median in bp3['medians']:
        median.set(color='#b2df8a', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp3['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    
    
    #plt.savefig(directory + '/' + cell + '/' + cell + '_overlap_boxplot3.png')
    plt.savefig(directory + '/' + 'All_overlap_boxplot3.svg')