def getRandomImage(filteredImagesCache=None, randomImageFilter=''):...
if not savedImagesCache:
generateSavedImagesCache(settings.settings['Output_dir'])
if filteredImagesCache:
randomImage = random.choice(filteredImagesCache)
randomImage = random.choice(savedImagesCache)
print('\tgetRandomImage(): Chose random image {} (filter {})'.format(
    randomImage, randomImageFilter))
serverPath = outputPathToServerPath(randomImage)
return randomImage, serverPath
