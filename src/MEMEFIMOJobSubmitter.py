__author__ = 'Jonathan Rubin'

import os
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
    shellscripttemplatedir = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO'
    packagedir = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    
    for TF in os.listdir(packagedir):
        if os.path.exists(packagedir + '/' + TF + '/peak_files/outfiles/MEME/combined.meme'):
            motiflist = run(packagedir + '/' + TF + '/peak_files/outfiles/MEME/combined.meme', True)
                    
            os.chdir(shellscripttemplatedir)
            for motif in motiflist:
                os.system("qsub -v arg1='/scratch/Shares/dowell/ENCODE/HCT116v2/" + TF + "/peak_files/outfiles/MEME/" + motif + "_fimo_out',arg2='" + motif + "',arg3='" + packagedir + "/" + TF + "/peak_files/outfiles/MEME/combined.meme' runMEMEFIMOTemplate.sh")
        
    