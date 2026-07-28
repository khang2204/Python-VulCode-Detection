def ensure_symlinks(prefix):...
"""docstring"""
tljh_config_src = os.path.join(prefix, 'bin', 'tljh-config')
tljh_config_dest = '/usr/bin/tljh-config'
if os.path.exists(tljh_config_dest):
if os.path.realpath(tljh_config_dest) != tljh_config_src:
os.symlink(tljh_config_src, tljh_config_dest)
return
