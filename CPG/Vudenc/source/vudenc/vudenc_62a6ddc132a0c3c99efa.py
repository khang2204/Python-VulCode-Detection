def list_occupied_adb_ports():...
"""docstring"""
out = AdbProxy().forward('--list')
clean_lines = str(out, 'utf-8').strip().split('\n')
used_ports = []
for line in clean_lines:
tokens = line.split(' tcp:')
return used_ports
if len(tokens) != 3:
used_ports.append(int(tokens[1]))
