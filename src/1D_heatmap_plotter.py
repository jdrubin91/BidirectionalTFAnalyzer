__author__ = 'Jonathan Rubin'

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import os

def run(filename,outdir):
    infoDict = dict()
    with open(filename) as file1:
        j = 0
        for line in file1:
            if not 'TF' in line:
                print j
                j += 1
                line = line.strip().split()
                TF = line[0]
                #SN = line[1]
                #p = line[2]
                #cent = line[3]
                #bimodal = line[4]
                x = line[2][0:len(line[2])-1].split(',')
                N = len(x)
                infoDict[TF] = [str(N)]
                #,SN,p,cent,bimodal]
                for i in range(N):
                    x[i] = float(x[i])/1500
    
                
                bins=100
                counts,edges = np.histogram(x, bins=bins)
                edges        = (edges[1:]+edges[:-1])/2. #bascially np.histogram gives you a list of start and stops of the bins, so we are just taking the center of the bins, so it matches the number of counts
                plt.bar(edges, counts, width=(edges[-1] - edges[0])/bins  )
            
                
                norm    = mpl.colors.Normalize(vmin=min(counts), vmax=max(counts))
                cmap    = cm.YlOrRd
                m       = cm.ScalarMappable(norm=norm, cmap=cmap)
                colors  = [m.to_rgba(c) for c in counts] 
                
                F    = plt.figure(figsize=(15,6))
                ax = F.add_axes([0,0,1,1])
                ax1  = F.add_subplot(1,1,1)
                ax1.bar(edges,np.ones((len(edges),)), color=colors, width=(edges[-1]-edges[0])/len(edges) , edgecolor=colors )
                #ax1.set_xlim(min(edges), max(edges))
                ax1.set_xlim(-1, 1)
                ax1.tick_params(
                    axis='x',          # changes apply to the x-axis
                    which='both',      # both major and minor ticks are affected
                    bottom='off',      # ticks along the bottom edge are off
                    top='off',         # ticks along the top edge are off
                    labelbottom='off') # labels along the bottom edge are off
                ax.tick_params(
                    axis='y',          # changes apply to the x-axis
                    which='both',      # both major and minor ticks are affected
                    right='off',      # ticks along the bottom edge are off
                    left='off',         # ticks along the top edge are off
                    labelbottom='off') # labels along the bottom edge are off
                ax.tick_params(
                    axis='x',          # changes apply to the y-axis
                    which='both',      # both major and minor ticks are affected
                    bottom='off',      # ticks along the bottom edge are off
                    top='off',         # ticks along the top edge are off
                    labelbottom='off') # labels along the bottom edge are off
                    
                F.patch.set_visible(False)
                ax.axis('off')
                #ax1.text(.325,.85,"uniform (SN): " + SN + "\nuniform (k-test): " + p + "\nmean = 0: " + cent + "\nbimodal(1=True): " + bimodal, fontsize = 18)
            
                #plt.title(TF + " (N = " + str(N) + ")", fontsize = 18)
                #plt.title(TF, fontsize = 18)
                #plt.xlabel("Distance to i", fontsize = 18)
                plt.gca().yaxis.set_major_locator(plt.NullLocator())
                if os.path.exists(outdir + '/' + TF + '.png'):
                    os.remove(outdir + '/' + TF + '.png')
                plt.savefig(outdir + '/' + TF)
                plt.close()
    #outfile = open(outdir + '/info.txt','w')
    #outfile.write("TF\tN\tEM S/N\tuniform p-val\tcentered at 0 p-val\tbimodal (1=True)\n")
    #for TF in infoDict:
    #    outfile.write(TF + "\t")
    #    for item in infoDict[TF]:
    #        outfile.write(item + "\t")
    #    outfile.write("\n")
            
if __name__ == "__main__":
    directory = '/scratch/Shares/dowell/TFIT/Danko2013/EMG_out_files/new_predictions/FIMO_OUT'
    for filename in os.listdir(directory):
        if '.EM' in filename:
            print filename
            outdir = directory + '/' + filename.split('.')[0] + '_notext'
            if not os.path.exists(outdir):
                os.mkdir(outdir)
            run(directory + '/' + filename,outdir)