def update_realfile(self, f, realfile):...
"""docstring"""
if not f[A_REALFILE] and os.path.exists(realfile) and not os.path.islink(
f[A_REALFILE] = realfile
