def print_all_syscalls(syscalls):...
for syscall_name, syscall_number in syscalls.items():
if syscall_number == -1:
print('{0:3} (0x{0:X}): {1}'.format(syscall_number, syscall_name))
