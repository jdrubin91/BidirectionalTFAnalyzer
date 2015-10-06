__author__ = 'Jonathan Rubin'

import Functions
import shutil
import os

def run(directory):
    directorylist = Functions.chip_peak_directories(directory)
    for directory1 in directorylist:
        os.chdir(directory1)
        RemoveList = [item for item in os.listdir(directory1) if 'ENC' not in item and 'SL' not in item]
        for item in RemoveList:
            if '.' in item:
                os.system("rm " + item)
            else:
                shutil.rmtree(directory1 + "/" + item)

if __name__ == '__main__':
    directory = '/projects/dowellLab/ENCODE/HCT116v2/'
    directorylist = Functions.chip_peak_directories(directory)
    for directory1 in directorylist:
        os.chdir(directory1)
        RemoveList = [item for item in os.listdir(directory1) if 'ENC' not in item]
        for item in RemoveList:
            if '.' in item:
                os.system("rm " + item)
            else:
                shutil.rmtree(directory1 + "/" + item)