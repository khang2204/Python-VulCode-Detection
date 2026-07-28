def set_mode(self, mode='svc'):...
modes = {value: key for key, value in self.modes.items()}
mask = modes[mode]
cpsr = int(self.get_register_value('cpsr', 'CPU', None), base=16)
self.set_register_value('cpsr', 'CPU', None, hex(int(str(bin(cpsr))[:-5] +
    mask, base=2)))
