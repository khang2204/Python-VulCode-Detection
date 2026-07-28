def write_file(path, contents):...
logger.info('writing %s', path)
if os.path.exists(path):
stat = os.stat(path)
mode, uid, gid = 420, -1, -1
mode, uid, gid = stat.st_mode, stat.st_uid, stat.st_gid
d = os.path.dirname(path)
os.path.exists(d) or os.makedirs(d)
newfile.write(contents)
os.chmod(newfile.name, mode)
os.chown(newfile.name, uid, gid)
os.rename(newfile.name, path)
