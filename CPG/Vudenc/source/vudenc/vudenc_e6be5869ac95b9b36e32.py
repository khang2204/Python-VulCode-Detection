def _delete_files(self, item):...
for file_col in self.get_file_column_list():
if self.is_file(file_col):
for file_col in self.get_image_column_list():
if getattr(item, file_col):
if self.is_image(file_col):
fm = FileManager()
if getattr(item, file_col):
fm.delete_file(getattr(item, file_col))
im = ImageManager()
im.delete_file(getattr(item, file_col))
