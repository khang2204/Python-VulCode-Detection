def parse_syscall_names():...
syscall_names = []
syscall_name_regex = re.compile('^.+SYS_(?P<syscall_name>[^ ]+)')
content = read_file_content(CONFIG['syscall_header_file'])
for line in content.split('\n'):
match = syscall_name_regex.match(line)
return syscall_names
if match:
syscall_names.append(match.group('syscall_name'))
