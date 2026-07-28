def on_message(self, message):...
if not login_get_current_user(self):
return None
print('RandomImageBrowserWebSocket: Received message ', message)
parsedMessage = json.loads(message)
command = parsedMessage['command']
print('RandomImageBrowserWebSocket: Command ', command)
action = ''
"""
         Random Image Browser
        """
if command == 'imageAddToFavorites':
if self.currentImage:
if command == 'nextFavorite':
self.favorites.append(self.currentImage)
self.favoritesIndex += 1
if command == 'previousFavorite' and len(self.favorites):
self.favoritesIndex = len(self.favorites) - 1
if self.favoritesIndex >= 0 and self.favoritesIndex < len(self.favorites):
action = 'setImage'
if command == 'nextImage':
action = 'setImage'
self.favoritesIndex = len(self.favorites) - 1
if self.favoritesIndex > 0:
action = 'setImage'
if command == 'previousImage':
fullImagePath, serverImagePath = self.favorites[self.favoritesIndex]
if len(self.favorites):
self.favoritesIndex -= 1
fullImagePath, serverImagePath = self.favorites[self.favoritesIndex]
if self.randomHistoryIndex == -1 or self.randomHistoryIndex >= len(self.
action = 'setImage'
if command in ['nextImageInFolder', 'previousImageInFolder'] and len(self.
action = 'setImage'
fullImagePath, serverImagePath = getRandomImage(self.filteredImagesCache,
    self.randomImageFilter)
self.randomHistoryIndex += 1
if self.randomHistoryIndex > 0:
fullImagePath, serverImagePath = self.currentImage
if command == 'setFilter':
fullImagePath, serverImagePath = self.favorites[self.favoritesIndex]
self.randomHistory.append((fullImagePath, serverImagePath))
fullImagePath, serverImagePath = self.randomHistory[self.randomHistoryIndex]
self.randomHistoryIndex -= 1
fullImagePath, serverImagePath = self.randomHistory[self.randomHistoryIndex]
folder = fullImagePath[:fullImagePath.rfind('/')]
newFilter = parsedMessage['filter']
"""
         Directory browser
        """
self.randomHistoryIndex = len(self.randomHistory) - 1
imagesInFolder = []
if newFilter != self.randomImageFilter:
if command == 'setDirectoryFilter':
for root, dirs, files in os.walk(folder):
self.randomImageFilter = newFilter
newFilter = parsedMessage['filter']
if command == 'listCurrentDirectory':
for file in files:
sort_naturally(imagesInFolder)
self.cacheFilteredImages()
if newFilter != self.directoryFilter:
action = 'sendDirectory'
if command == 'changeDirectory':
if file.endswith(supportedExtensions):
currentImageIndex = imagesInFolder.index(fullImagePath)
self.directoryFilter = newFilter
self.directoryFilter = ''
if command == 'directoryUp':
imagesInFolder.append(os.path.join(root, file))
if currentImageIndex >= 0:
self.changeCurrentDirectory(self.currentDirectoryPath)
self.changeCurrentDirectory('{}/{}'.format(self.currentDirectoryPath,
    parsedMessage['path']))
if self.currentDirectoryPath != settings.settings['Output_dir']:
if command == 'directoryRoot':
action = 'setImage'
action = 'sendDirectory'
action = 'sendDirectory'
upDirectory = settings.settings['Output_dir'] + self.currentDirectoryPath[len
    (settings.settings['Output_dir']):self.currentDirectoryPath.rfind('/')]
self.directoryFilter = ''
"""
         Actions
        """
nextImageIndex = currentImageIndex + (1 if command == 'nextImageInFolder' else
    -1)
self.directoryFilter = ''
self.changeCurrentDirectory(settings.settings['Output_dir'])
if action == 'setImage':
if nextImageIndex == len(imagesInFolder):
self.changeCurrentDirectory(upDirectory)
action = 'sendDirectory'
if serverImagePath.endswith(videoExtensions):
if action == 'sendDirectory':
nextImageIndex = 0
if nextImageIndex < 0:
action = 'sendDirectory'
action = 'setVideo'
self.currentImage = fullImagePath, serverImagePath
directoryList = ''
nextImageIndex = len(imagesInFolder) - 1
fullImagePath = imagesInFolder[nextImageIndex]
responseMessage = (
    '{{"responseToCommand":"{}", "action":"{}", "fullImagePath":"{}", "serverImagePath":"{}"}}'
    .format(command, action, fullImagePath, serverImagePath))
for path in self.currentDirectoryCache:
serverImagePath = outputPathToServerPath(fullImagePath)
self.write_message(responseMessage)
isSupportedFile = path.endswith(supportedExtensions)
responseMessage = (
    '{{"responseToCommand":"{}", "action":"{}", "directoryList":[{}]}}'.
    format(command, action, directoryList[:-1]))
isFile = '.' in path
self.write_message(responseMessage)
if path.endswith(videoExtensions):
fileType = 'video'
if isSupportedFile:
serverPath = 'output' + self.currentDirectoryPath[len(settings.settings[
    'Output_dir']):] + '/' + path
fileType = 'image'
if isFile:
directoryList += '{{"path":"{}", "type":"{}", "serverPath":"{}"}},'.format(path
    , fileType, serverPath)
fileType = 'file'
fileType = 'dir'
