def get_shared_memory_bytes():...
"""docstring"""
assert sys.platform == 'linux' or sys.platform == 'linux2'
shm_fd = os.open('/dev/shm', os.O_RDONLY)
shm_fs_stats = os.fstatvfs(shm_fd)
os.close(shm_fd)
return shm_avail
shm_avail = shm_fs_stats.f_bsize * shm_fs_stats.f_bavail
