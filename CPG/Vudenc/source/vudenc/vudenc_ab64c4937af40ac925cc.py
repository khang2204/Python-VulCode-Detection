def remove(file):...
if os.path.exists(file):
if os.path.isdir(file):
os.remove(file)
os.removedirs(file)
