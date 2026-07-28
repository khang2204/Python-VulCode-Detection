def load_bumplimit_set(self):...
if not os.path.isfile(self.bumplimitfile):
return
self.pc.sets['bumplimit'].update(pickle.loads(f.read()))
