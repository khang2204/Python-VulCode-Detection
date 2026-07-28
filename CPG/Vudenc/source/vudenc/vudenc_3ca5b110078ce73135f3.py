def isASuccessfulUpload(self, html):...
result = False
validExt = False
if self.notRegex:
fileUploaded = re.search(self.notRegex, html)
if self.trueRegex and not result:
if fileUploaded == None:
fileUploaded = re.search(self.trueRegex, html)
return result
result = True
if fileUploaded:
if self.trueRegex:
result = str(fileUploaded.group(1))
result = str(fileUploaded.group(0))
moreInfo = re.search(self.trueRegex, html)
if moreInfo:
result = str(moreInfo.groups())
