def generate_syscalls(syscall_names, bitness):...
syscalls = {}
for syscall_name in syscall_names:
syscalls[syscall_name] = get_syscall_number(syscall_name, bitness)
return OrderedDict(sorted(syscalls.items(), key=itemgetter(1)))
