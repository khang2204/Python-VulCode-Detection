def get_path_string(self):...
if len(self.path) == 1:
return '/'
directory_ids_string = ', '.join([str(each) for each in self.path])
directories = db.select('directory', 'id in (' + directory_ids_string + ')')
return '/'.join([directory['name'] for directory in directories])[1:]
