#!/usr/bin/env python3

import os

ext = ".py"

def  getFileList(filepath,ext):
    _filelist = []
    for cur, _dirs, files in os.walk(filepath):
        print(cur)
        print(_dirs)
        print(files)
        print(list(os.walk(filepath)))
        for filenm in files:
            if (filenm.lower()).endswith(ext.lower()):
                _filelist.append(cur+"\\"+filenm)
    return _filelist
a = getFileList("./",ext)
print(a)