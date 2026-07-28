def __init__(self, **kwargs):...
super().__init__(**kwargs)
self.argv = list(sys.argv)
self.cwd = os.getcwd()
