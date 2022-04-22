
from pathlib import Path
import csv
import os
import sys
import hashlib

def helper(path, cad):
    if Path(path).is_file():
        if not path.endswith('.sldprt'):
            return;
        else:
            with open(path,'rb') as f:
                fRead = f.read()
                cad[path] = hashlib.sha256(fRead).hexdigest()
    else:
        forkDir = os.listdir(path)
        for file in forkDir:
            nextDir = path + '/' + file
            if nextDir.endswith('.csv'):
                continue
            #print(nextDir)
            helper(nextDir,cad)
    return cad

def CAD(path):
    cad = dict()
    if Path(path).is_file():
        print("the input is not a directory\n")
    helper(path,cad)
    return cad

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parent = sys.argv[1]
    childDir = os.listdir(parent)
    bomFile = 0
    for file in childDir:
        if file.endswith('.csv'):
            bomFile = file
            break

    if bomFile == 0:
        print("error: missing BOM file\n")
    cad = dict()
    cad = CAD(parent)
    os.chdir(parent)

    error = 0
    bomFile = open(bomFile)
    bom = csv.reader(bomFile)
    bomDict = dict()

    firstRow = 1
    for row in bom:
        if firstRow == 1:
            firstRow = 0
            continue
        bomDict[row[0]] = row[1]

    fileName = dict()
    for path in cad.keys():
        Duplicate = 0
        lastSlashIndex = path.rfind("/")
        file = ''
        if lastSlashIndex < len(path)-1:
            file = path[lastSlashIndex+1:]
        else:
            print("wrong file name")
            error = 1
            continue

        if file not in bomDict.keys():
            print("MISSING: "+ file)
            error = 1
            continue

        for key,value in fileName.items():
            if value == file:
                Duplicate = 1
                error = 1
                print("DUPLICATE: " + key)

        if Duplicate == 1:
            error = 1
            print("DUPLICATE: "+path)
            Duplicate = 0
            continue

        else:
            fileName[path] = file

        if file not in bomDict.keys():
            error = 1
            print("UNIDENTIFIED: " + path + "not in BOM.sqlprt")
            continue

        if cad[path] != bomDict[file]:
            error = 1
            print("MODIFIED: " + path)
            continue

    if error == 0:
        print("OK")

    bomFile.close()


