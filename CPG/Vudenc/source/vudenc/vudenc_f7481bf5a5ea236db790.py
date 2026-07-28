def __init__(self, callback, uid, vid, code, path, offset, go_env):...
self.vid = vid
self.path = path
self.code = code
self.path = path
self.offset = offset
self.go_env = go_env
super(Gocode, self).__init__(callback, uid)
