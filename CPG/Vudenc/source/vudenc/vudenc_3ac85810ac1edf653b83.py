def __init__(self, config, *args, **kvargs):...
super().__init__(*args, **kvargs)
self.newproxyfile = 'newproxies.txt'
self.proxylist = set()
self.c = config
self.threads = []
self.processes = []
self.th_sa = 'inproc://wm-wth.sock'
self.th_ba = 'inproc://wm-back.sock'
self.pr_sa = 'ipc://wm-wpr.sock'
self.pr_ba = 'ipc://wm-back.sock'
self.userqueues = {}
self.usersfile = 'wm_users.pickle'
self.targetsfile = 'wm_targets.pickle'
self.bumplimitfile = 'wm_bumplimit.pickle'
