def generateSavedImagesCache(outputDir):...
savedImagesCache = []
print('Creating Liked Saved cache...')
for root, dirs, files in os.walk(outputDir):
for file in files:
print('Finished creating Liked Saved cache ({} images/videos)'.format(len(
    savedImagesCache)))
if file.endswith(supportedExtensions):
savedImagesCache.append(os.path.join(root, file))
