def __init__(self, wires, *, shots=0, cutoff=None, hbar=2):...
self.wires = wires
self.cutoff = cutoff
self.hbar = hbar
self.eng = None
self.state = None
super().__init__(self.short_name, shots)
