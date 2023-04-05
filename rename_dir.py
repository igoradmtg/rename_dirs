import os
pathDirs = r"d:\upl1"
pathDirsNew = r"d:\upl2"
dirs = []
dirsRename = []
for address, dirs, files in os.walk(pathDirs):
    if len(files)>0 and len(dirs)==0:
        print(f"{address}")
        newName = os.path.join(pathDirsNew,os.path.basename(address))
        print(f"{newName}")
        dirsRename.append({'OldName':address,'NewName':newName})
        
print(dirsRename)
for dirInfo in dirsRename:
    os.rename(dirInfo['OldName'],dirInfo['NewName'])
