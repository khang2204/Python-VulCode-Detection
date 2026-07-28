def createZip(src, dst):...
zf = zipfile.ZipFile('%s' % dst, 'w')
abs_src = os.path.abspath(src)
for dirname, subdirs, files in os.walk(src):
for filename in files:
zf.close()
if filename != backdoor:
absname = os.path.abspath(os.path.join(dirname, filename))
arcname = absname[len(abs_src) + 1:]
zf.write(absname, arcname)
