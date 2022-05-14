import zipfile
import sys
import os
import re
import hashlib as md5
def main():
    action = sys.argv[1]
    if action == "UZ":
        UnzipFiles(sys.argv[2])
    if action == "DD":
        remove_duplicates(sys.argv[2])
def UnzipFiles(file):
    zipdata = zipfile.ZipFile()
    zipinfos = zipdata.infolist()
    for zipinfo in zipinfos:
        zipinfo.filename = renameToShortName(zipinfo.filename)
        print ("Unzipping file"+zipinfo.filename)
        zipdata.extract(zipinfo)

def renameToShortName(name):
    if(len(name)>260):
        name=name[0:259]
    return name

def remove_duplicates(dir):
    unique = []
    count = 0
    for filename in os.listdir(dir):
        onlyFilename = ""
        if filename.endswith('.epub'):
            onlyFilename = filename[:-5]
        #print("Reading file "+filename)
        onlyAplhaFileName = re.sub(r'[^a-zA-Z]', '', onlyFilename)
       # print("Only alphabets "+onlyAplhaFileName)
       # print(filename)
        if os.path.isfile(dir+"/"+filename):
            print("File is file"+filename)
            filehash = md5.md5(onlyAplhaFileName).hexdigest()
            if filehash not in unique: 
                unique.append(filehash)
            else: 
                print("Deleting file "+filename)
                count+=1
                os.remove(dir+"/"+filename)
    print(count)

if __name__ == "__main__":
    main()