def expectation(self, observable, wires):...
pq.ops.R(0) | self.reg[0]
pq.ops.All(pq.ops.Measure) | self.reg
self.eng.flush()
if observable == 'PauliZ':
probabilities = self.eng.backend.get_probabilities([self.reg[wires]])
if observable == 'AllPauliZ':
if '1' in probabilities:
probabilities = self.eng.backend.get_probabilities(self.reg)
return expectation_value
expectation_value = 2 * probabilities['1'] - 1
expectation_value = -(2 * probabilities['0'] - 1)
expectation_value = [(2 * sum(p for state, p in probabilities.items() if 
    state[i] == '1') - 1 - (2 * sum(p for state, p in probabilities.items() if
    state[i] == '0') - 1)) for i in range(len(self.reg))]
variance = 1 - expectation_value ** 2
variance = [(1 - e ** 2) for e in expectation_value]
