def noremote_ref(self):...
nr_ref = self.ref
if '/' in nr_ref:
nr_ref = nr_ref.split('/', 1)[1]
return nr_ref
