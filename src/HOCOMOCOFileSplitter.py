__author__ = 'Jonathan Rubin'

import os
import Functions

def run(filename1, header):
    file1 = open(filename1)
    headerlist = []
    motifdict = dict()
    if header != False:
        line1 = file1.readline()
        while 'MOTIF' not in line1:
            headerlist.append(line1)
            line1 = file1.readline()
        motif = line1
        motifdict[motif] = []
    for line2 in file1:
        if 'MOTIF' in line2:
            motif = line2
            motifdict[motif] = []
        else:
            motifdict[motif].append(line2)
    
    return motifdict,headerlist

if __name__ == "__main__":
    
    shellscripttemplatedir = '/Users/joru1876/HOCOMOCODatabaseFIMO'
    packagedir = '/Users/joru1876/BidirectionalTFAnalyzer'
    
    
    motifdict,headerlist = run(packagedir + '/files/HOCOMOCOv9_AD_MEME.txt', True)
    if not os.path.exists(packagedir + '/files/HOCOMOCOFileSplitterout'):
        os.mkdir(packagedir + '/files/HOCOMOCOFileSplitterout')
    for motif in motifdict:
        outfile = open(packagedir + '/files/HOCOMOCOFileSplitterout/' + motif.strip().split()[1] + '.txt','w')
        for hitem in headerlist:
            outfile.write(hitem)
        outfile.write(motif)
        for mitem in motifdict[motif]:
            outfile.write(mitem)
            
    
    
    motiflist = os.listdir(packagedir + '/files/HOCOMOCOFileSplitterout')
    os.chdir(shellscripttemplatedir)
    for motif in motiflist:
        os.system("qsub -v arg1='/Users/joru1876/HOCOMOCODatabaseFIMO/" + motif.split('.')[0] + "_fimo_out',arg2='" + motif.split('.')[0] + "' runHOCOMOCOv9FIMOTemplate.sh")
        
    