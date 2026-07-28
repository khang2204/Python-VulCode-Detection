def metadata_conflicting(self, b):...
a = self.to_dict()
for comp in ['title', 'size', 'tags', 'torrent_date', 'tracker_info']:
if comp not in b or str(a[comp]) == str(b[comp]):
return False
return True
