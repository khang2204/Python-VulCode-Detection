def get_system_memory():...
"""docstring"""
docker_limit = None
memory_limit_filename = '/sys/fs/cgroup/memory/memory.limit_in_bytes'
if os.path.exists(memory_limit_filename):
docker_limit = int(f.read())
psutil_memory_in_bytes = None
import psutil
if psutil_memory_in_bytes is not None:
psutil_memory_in_bytes = psutil.virtual_memory().total
memory_in_bytes = psutil_memory_in_bytes
if sys.platform == 'linux' or sys.platform == 'linux2':
if docker_limit is not None:
bytes_in_kilobyte = 1024
memory_in_bytes = sysctl(['sysctl', 'hw.memsize'])
return min(docker_limit, memory_in_bytes)
return memory_in_bytes
memory_in_bytes = vmstat('total memory') * bytes_in_kilobyte
