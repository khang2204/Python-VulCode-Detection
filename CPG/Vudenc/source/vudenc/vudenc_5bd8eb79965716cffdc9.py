def remove_directories(self, directory_ids):...
directory_ids_string = ', '.join([str(each) for each in directory_ids])
for directory_id in directory_ids:
content = self.get_directory_content(directory_id)
db.delete('directory', 'id in (' + directory_ids_string + ')')
self.remove_files([each['id'] for each in content['files']])
self.remove_directories([each['id'] for each in content['directories']])
