def __init__(self, wires, *, shots=0):...
self.wires = wires
self.eng = None
self._state = None
super().__init__(self.short_name, shots)
