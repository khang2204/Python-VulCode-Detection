def get_register_value(self, register, target, target_index):...
if 'memory_mapped' in self.targets[target] and self.targets[target][
command = 'md'
buff = self.command('rd ' + register, [':'], 'Error getting register value')
if 'bits' in self.targets[target]['registers'][register]:
return buff.split('\r')[0].split(':')[1].split()[0]
bits = self.targets[target]['registers'][register]['bits']
address = self.targets[target]['base'][target_index] + self.targets[target][
    'registers'][register]['offset']
if bits == 8:
buff = self.command(command + ' ' + hex(address) + ' 1', [':'],
    'Error getting register value')
command += 'b'
if bits == 16:
command += 'h'
if bits == 64:
command += 'd'
