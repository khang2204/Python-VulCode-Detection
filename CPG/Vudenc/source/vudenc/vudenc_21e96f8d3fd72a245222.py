def apply(self, gate_name, wires, *par):...
if gate_name not in self._gates:
gate = operator_map[gate_name](*par)
if isinstance(wires, int):
gate | self.reg[wires]
gate | tuple([self.reg[i] for i in wires])
