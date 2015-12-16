__author__ = 'Jonathan Rubin'

import os
import Functions

#Populates FIMO_Files directory with fimo.txt files for each TF, renames fimo 
#files as TF.txt

#def run():
#    
#    return
    
if __name__ == "__main__":
    directory = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_OUT_v10'
    outfiledir = '/scratch/Shares/dowell/ENCODE/HOCOMOCODatabaseFIMO/FIMO_Files_v10'
    
    for fimodir in os.listdir(directory):
        TF = fimodir.split('/')[len(fimodir.split('/'))]
        fulldir = directory + '/' + fimodir + '/fimo.txt'
        os.system("cat " + fulldir + " > " + outfiledir + "/" + TF + ".txt")
    
    #for fimodir in Functions.HOCOMOCO_fimo_directories(directory):
    #    TF = fimodir.split('/')[len(fimodir.split('/'))-1]
    #    os.system("cat " + fimodir + "/fimo.txt > " + outfiledir + "/" + TF + ".txt")