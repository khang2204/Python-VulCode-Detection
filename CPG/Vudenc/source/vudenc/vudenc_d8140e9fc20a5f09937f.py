def getCaptionPic(self, pth):...
"""docstring"""
pth = path.join(path.dirname(pth), METADATA_FILENAME)
data = self.getCaption(pth)
return data
