__author__ = 'Jonathan Rubin'

import os
import time
import Functions

def run(filename1, header):
    file1 = open(filename1)
    motiflist = []
    for line1 in file1:
        if 'MOTIF' in line1:
            motif = line1.strip().split()[1]
            motiflist.append(motif)
    
    return motiflist

if __name__ == "__main__":
    
    #Right now this calls fimo on each motif by providing the HOCOMOCO database along with a single motif name per
    #job submitted. It now only submits jobs for motifs who have fimo.txt files less than 1
    shellscripttemplatedir = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO'
    packagedir = '/scratch/Users/joru1876/BidirectionalTFAnalyzer'
    
    
    motiflist = run(packagedir + '/files/HOCOMOCOv10_HUMAN_mono_meme_format.meme', True)
    motiflist1 = []
    for item in motiflist:
        if not os.path.exists(shellscripttemplatedir + "/FIMO_OUT_HCT116/" + item + "_fimo_out"):
        #    os.mkdir(shellscripttemplatedir + "/FIMO_OUT_v10/" + '_'.join(item.split('.')) +"_fimo_out")
        #if Functions.line_count(shellscripttemplatedir + "/FIMO_OUT_v10/" + '_'.join(item.split('.')) +"_fimo_out"+ "/fimo.txt") < 2:
            motiflist1.append(item)
    
    print motiflist1
    print len(motiflist1)
            
    os.chdir(shellscripttemplatedir)
    i = 1
    for motif in motiflist1:
        os.system("qsub -v arg1='/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_OUT_HCT116/" + motif + "_fimo_out',arg2='" + motif + "' runHOCOMOCO_HCT116_FIMOTemplate.sh")
        if i%100 == 0:
            time.sleep(36000)
        i+=1
    