def set_register_value(self, register, target, target_index, value):...
if 'memory_mapped' in self.targets[target] and self.targets[target][
command = 'mm'
self.command('rm ' + register + ' ' + value, error_message=
    'Error setting register value')
if 'bits' in self.targets[target]['registers'][register]:
bits = self.targets[target]['registers'][register]['bits']
address = self.targets[target]['base'][target_index] + self.targets[target][
    'registers'][register]['offset']
if bits == 8:
self.command(command + ' ' + hex(address) + ' ' + value + ' 1',
    error_message='Error getting register value')
command += 'b'
if bits == 16:
command += 'h'
if bits == 64:
command += 'd'
