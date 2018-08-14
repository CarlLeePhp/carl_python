#!/usr/bin/python3

import os

# os.walk method
for folderName, subfolders, filenames in os.walk('/home/likunhui/Downloads/'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('Subfold of ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)

    print('')