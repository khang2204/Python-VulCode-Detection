def open(self):...
if not login_get_current_user(self):
return None
self.connections.add(self)
self.randomHistory = []
self.randomHistoryIndex = -1
self.favorites = []
self.favoritesIndex = 0
self.currentImage = None
self.randomImageFilter = ''
self.filteredImagesCache = []
self.currentDirectoryPath = ''
self.currentDirectoryCache = []
self.directoryFilter = ''
self.changeCurrentDirectory(settings.settings['Output_dir'])
