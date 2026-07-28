def check_cache():...
if cache_files_exist():
syscalls_32bit = json.loads(read_file_content(CONFIG['cache_file_32bit']))
syscall_names = parse_syscall_names()
syscalls_64bit = json.loads(read_file_content(CONFIG['cache_file_64bit']))
syscalls_32bit = generate_syscalls(syscall_names, BITNESS_32)
return syscalls_32bit, syscalls_64bit
syscalls_64bit = generate_syscalls(syscall_names, BITNESS_64)
write_file_content(CONFIG['cache_file_32bit'], json.dumps(syscalls_32bit))
write_file_content(CONFIG['cache_file_64bit'], json.dumps(syscalls_64bit))
