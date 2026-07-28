def check_cache_directory():...
directory = '{}/.cache/syscall_number'.format(os.environ['HOME'])
if not pathlib.Path(directory).exists():
os.mkdir(directory)
