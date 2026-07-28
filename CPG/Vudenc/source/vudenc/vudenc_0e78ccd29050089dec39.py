def get_directory_content(self, directory_id=None):...
if not directory_id:
directory_id = self.path[-1:][0]
return {'directories': db.select('directory', 'parent_directory_id = ' +
    str(directory_id) + ' AND user_id = ' + str(self.user_id)), 'files': db
    .select('file', 'directory_id = ' + str(directory_id) +
    ' AND user_id = ' + str(self.user_id))}
