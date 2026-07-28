def get_filesize(self, file):...
file.seek(0, 2)
size = file.tell()
file.seek(0)
return size
