def pdf_url(self):...
dg = self.data_group
fn = self.get_abstract_filename()
return f'/media/{dg.fs_id}/pdf/{fn}'
