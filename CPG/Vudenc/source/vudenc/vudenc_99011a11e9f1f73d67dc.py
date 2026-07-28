def cacheFilteredImages(self):...
self.filteredImagesCache = []
if not self.randomImageFilter:
return
randomImageFilterLower = self.randomImageFilter.lower()
for imagePath in savedImagesCache:
if randomImageFilterLower in imagePath.lower():
print('\tFiltered images with "{}"; {} images matching filter'.format(self.
    randomImageFilter, len(self.filteredImagesCache)))
self.filteredImagesCache.append(imagePath)
