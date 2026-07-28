def changeCurrentDirectory(self, newDirectory):...
self.currentDirectoryPath = newDirectory
dirList = os.listdir(self.currentDirectoryPath)
filteredDirList = []
for fileOrDir in dirList:
if not fileOrDir.endswith('.json') and (not self.directoryFilter or self.
self.currentDirectoryCache = sorted(filteredDirList)
filteredDirList.append(fileOrDir)
