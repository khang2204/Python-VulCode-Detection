def get_register_value(self, register, target, target_index):...
if target == 'CP':
buff = self.command(' '.join(['arm', 'mrc', str(self.targets[target][
    'registers'][register]['CP']), str(self.targets[target]['registers'][
    register]['Op1']), str(self.targets[target]['registers'][register][
    'CRn']), str(self.targets[target]['registers'][register]['CRm']), str(
    self.targets[target]['registers'][register]['Op2'])]), error_message=
    'Error getting register value')
buff = self.command('reg ' + register, [':'], 'Error getting register value')
return hex(int(buff.split('\n')[1].strip()))
return buff.split('\n')[1].split(':')[1].split()[0]
