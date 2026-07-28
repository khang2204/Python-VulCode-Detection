def print_single_syscall(syscall_name, syscalls, quiet):...
if syscall_name not in syscalls.keys():
if quiet:
print(syscalls[syscall_name])
print('The syscall number for {0} is: {1} (0x{1:X})'.format(syscall_name,
    syscalls[syscall_name]))
