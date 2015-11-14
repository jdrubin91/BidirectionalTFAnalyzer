__author__ = 'Jonathan Rubin'

import os
import Functions

def run(fimodir):
    
    fimofile = fimodir + '/fimo.txt'
    
    Functions.cut_file(fimofile, [1,2,3], fimodir + '/fimo.cut.txt')
    
    
    return Functions.parse_file(fimodir + '/fimo.cut.txt')[1:len(Functions.parse_file(fimodir + '/fimo.cut.txt'))]
    
if __name__ == "__main__":
    directory = '/scratch/Shares/dowell/ENCODE/HCT116v2'
    
    for TF in os.listdir(directory):
        if os.path.exists(directory + '/' + TF + '/peak_files/outfiles/MEME'):
            for fimofolder in [i for i in os.listdir(directory + '/' + TF + '/peak_files/outfiles/MEME') if 'fimo_out' in i and i[0].isdigit()]:
                fimodir = directory + '/' + TF + '/peak_files/outfiles/MEME/' + fimofolder
                fimodict = dict()
                fimodict[fimofolder] = run(fimodir)
            outfile = open(directory + '/' + TF + '/peak_files/outfiles/MEME/fimo.cat.txt','w')
            for key in fimodict:
                for item in fimodict[key]:
                    for val in item:
                        outfile.write(val)
                        outfile.write('\t')
                    outfile.write(key)
                    outfile.write('\n')