def __init__(self, path):...
self.path = path
self.abspath = settings.STORAGE_DIR + path
self.meta = ImageMetadata(self.abspath)
self.meta.read()
