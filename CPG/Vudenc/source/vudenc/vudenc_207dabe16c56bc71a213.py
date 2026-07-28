def __init__(self, ev_init, *args, **kvargs):...
super().__init__()
self.ev_init = ev_init
self.bind_kt_ticker = Ticker()
self.bind_kt = 5
