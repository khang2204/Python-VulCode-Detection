def __init__(self, wires, *, shots=0, hbar=2):...
self.wires = wires
self.hbar = hbar
self.eng = None
self.state = None
super().__init__(self.short_name, shots)
