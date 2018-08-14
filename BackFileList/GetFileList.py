#!/usr/bin/python3

import os, csv

# vars


os.chdir("/home/likunhui/test")
outputFile = open('FileList.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['file name', 'fold name'])

# os.walk method
for folderName, subfolders, filenames in os.walk('/home/likunhui/Downloads/'):
    for filename in filenames:
        outputWriter.writerow([filename, folderName])

outputFile.close()