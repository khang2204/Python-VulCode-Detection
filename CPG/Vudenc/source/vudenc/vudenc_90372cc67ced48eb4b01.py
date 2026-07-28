def protect(self):...
mode = lstat(self.file).st_mode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH
if os.path.isdir(self.file):
for root, dirs, files in os.walk(self.file):
lchmod(self.file, mode)
for d in dirs:
lchmod(os.path.join(self.file, d), mode)
for f in files:
lchmod(os.path.join(self.file, f), mode)
