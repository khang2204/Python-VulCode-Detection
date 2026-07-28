def set_register_value(self, register, target, target_index, value):...
if target == 'CP':
self.command(' '.join(['arm', 'mrc', str(self.targets[target]['registers'][
    register]['CP']), str(self.targets[target]['registers'][register]['Op1'
    ]), str(self.targets[target]['registers'][register]['CRn']), str(self.
    targets[target]['registers'][register]['CRm']), str(self.targets[target
    ]['registers'][register]['Op2']), value]), error_message=
    'Error setting register value')
self.command('reg ' + register + ' ' + value, error_message=
    'Error setting register value')
