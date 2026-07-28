def read_file(self):...
lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [line for line in lines if line and not line.startswith('#')]
lines = '\n'.join(lines).replace('\\\n', '').split('\n')
for line in lines:
line = shlex.split(line, True)
print_warning('%s : Could not parse this line (%s) : %s' % (self.path, e, line)
    )
yield line
