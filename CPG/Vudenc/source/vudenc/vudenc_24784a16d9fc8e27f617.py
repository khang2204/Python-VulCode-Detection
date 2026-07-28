def expectation(self, observable, wires):...
self.eng.flush(deallocate_qubits=False)
if observable == 'PauliX' or observable == 'PauliY' or observable == 'PauliZ':
expectation_value = self.eng.backend.get_expectation_value(pq.ops.
    QubitOperator(str(observable)[-1] + '0'), self.reg)
if observable == 'AllPauliZ':
variance = 1 - expectation_value ** 2
expectation_value = [self.eng.backend.get_expectation_value(pq.ops.
    QubitOperator('Z' + '0'), [qubit]) for qubit in self.reg]
return expectation_value
variance = [(1 - e ** 2) for e in expectation_value]
