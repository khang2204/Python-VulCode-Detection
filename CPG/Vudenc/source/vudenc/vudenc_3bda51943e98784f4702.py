def __init__(self, wires, **kwargs):...
kwargs.setdefault('shots', 0)
super().__init__(self.short_name, kwargs['shots'])
for k, v in {'log': 'verbose'}.items():
if k in kwargs:
if 'num_runs' in kwargs:
kwargs.setdefault(v, kwargs[k])
if isinstance(kwargs['num_runs'], int) and kwargs['num_runs'] > 0:
self.wires = wires
self.n_eval = kwargs['num_runs']
self.n_eval = 0
self.backend = kwargs['backend']
self.kwargs = kwargs
self.eng = None
self.reg = None
