def cp(src, dst):...
r, f = os.path.split(dst)
mkdir_p(r)
shutil.copy2(src, dst)
