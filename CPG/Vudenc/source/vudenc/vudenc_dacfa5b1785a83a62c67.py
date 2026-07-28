def on_circuit_removed(self, subject, changetype, circuit, *args):...
if isinstance(circuit, Circuit):
event = {'circuit_id': circuit.circuit_id, 'bytes_up': circuit.bytes_up,
    'bytes_down': circuit.bytes_down, 'uptime': time.time() - circuit.
    creation_time}
self.write_data({'type': 'circuit_removed', 'event': event})
