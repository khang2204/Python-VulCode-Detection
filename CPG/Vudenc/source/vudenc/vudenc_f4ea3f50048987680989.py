def print_man_page_info(syscall_name):...
man_environment_variables = {'MANPAGER': 'cat', 'COLUMNS': '80'}
command = 'man 2 {}'.format(syscall_name)
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, env=
    man_environment_variables)
stdout, _ = process.communicate()
stdout = stdout.decode()
information_regex = re.compile('(NAME(.|\\n)+)\\n\\nDESCRIPTION')
match = information_regex.search(stdout)
if match:
man_text = '\n'
man_text = 'no man page info available'
man_text += match.group(1)
print(man_text)
man_text += """

...for more details run "{}\"""".format(command)
