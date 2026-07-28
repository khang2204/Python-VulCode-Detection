def _create_request(self, command, **args):...
seq = self._seq
self._seq += 1
return {'type': 'request', 'seq': seq, 'command': command, 'arguments': args}
