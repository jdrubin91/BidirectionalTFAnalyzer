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
    
    #Right now this writes a folder called HOCOMOCOFileSplitterout which contains a single txt file for each motif in HOCOMOCO database (with appropriate header)
    #Since FIMO was still having trouble recognizing the motif files, I opted to instead just get motif names from the database and do seperate FIMO submissions
    #for each motif (but still using the same database motif file for each one).  As of right now I could eliminat 
    shellscripttemplatedir = '/Users/joru1876/HOCOMOCODatabaseFIMO'
    packagedir = '/Users/joru1876/BidirectionalTFAnalyzer'
    
    
    motiflist = run(packagedir + '/files/HOCOMOCOv9_AD_MEME.txt', True)
    motiflist1 = []
    for item in motiflist:
        if not os.path.exists(shellscripttemplatedir + "/FIMO_OUT/" + item +"_fimo_out"+ "/fimo.txt"):
            motiflist1.append(item)
    
    print motiflist1
    print len(motiflist1)
            
    os.chdir(shellscripttemplatedir)
    for motif in motiflist1:
        os.system("qsub -v arg1='/Users/joru1876/HOCOMOCODatabaseFIMO/" + motif + "_fimo_out',arg2='" + motif + "' runHOCOMOCOv9FIMOTemplate.sh")
        
    