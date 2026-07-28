def __init__(self, forums, targets, sbjfun, msgfun, *args, **kvargs):...
self.sbjfun = sbjfun
self.msgfun = msgfun
self.forums = forums
self.targets = type(targets) == str and [('', targets)] or type(targets
    ) == tuple and list(targets) or targets
super().__init__(*args, **kvargs)
