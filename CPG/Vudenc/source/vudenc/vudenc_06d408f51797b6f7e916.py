def __init__(self, fs, cfg):...
self.fs = fs
self.cfg = cfg
self.tempfiles = {}
self.filenames = {}
self.newcount = 0
self.init_honeyfs(self.cfg.get('honeypot', 'contents_path'))
