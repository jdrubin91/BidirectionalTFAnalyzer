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
    shellscripttemplatedir = '/Users/joru1876/HOCOMOCODatabaseFIMO'
    packagedir = '/Users/joru1876/BidirectionalTFAnalyzer'
    
    
    motiflist = run(packagedir + '/files/HOCOMOCOv9_AD_MEME.txt', True)
    motiflist1 = []
    for item in motiflist:
        if not os.path.exists(shellscripttemplatedir + "/FIMO_OUT/" + item +"_fimo_out"+ "/fimo.txt") or Functions.line_count(shellscripttemplatedir + "/FIMO_OUT/" + item +"_fimo_out"+ "/fimo.txt") < 2:
            motiflist1.append(item)
    
    print motiflist1
    print len(motiflist1)
            
    os.chdir(shellscripttemplatedir)
    for motif in motiflist1:
        os.system("qsub -v arg1='/Users/joru1876/HOCOMOCODatabaseFIMO/FIMO_OUT/" + motif + "_fimo_out',arg2='" + motif + "' runHOCOMOCOv9FIMOTemplate.sh")
        
    