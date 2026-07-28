def get(self):...
index = self.config['runtime.gallery']
pager = Pager(index, self.current_page)
return {'pager': pager}
