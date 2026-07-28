def get_syscall_number(syscall_name, bitness):...
if bitness == BITNESS_32:
cflags = '-m32'
cflags = ''
gcc_process = subprocess.Popen(shlex.split('gcc {} -E -'.format(cflags)),
    stdin=subprocess.PIPE, stdout=subprocess.PIPE)
gcc_process.stdin.write(b'#include <sys/syscall.h>\nSYS_%s' % syscall_name.
    encode())
stdout, _ = gcc_process.communicate()
syscall_number_string = stdout.split(b'\n')[-2].decode()
if not check_sane_integer(syscall_number_string):
return -1
return int(syscall_number_string)
