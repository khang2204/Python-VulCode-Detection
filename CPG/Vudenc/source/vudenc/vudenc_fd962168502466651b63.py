def __init__(self, wires, **kwargs):...
if 'user' not in kwargs:
if 'password' not in kwargs:
kwargs['backend'] = 'IBMBackend'
super().__init__(wires, **kwargs)
