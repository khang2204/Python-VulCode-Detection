def _add_files(self, this_request, item):...
fm = FileManager()
im = ImageManager()
for file_col in this_request.files:
if self.is_file(file_col):
for file_col in this_request.files:
fm.save_file(this_request.files[file_col], getattr(item, file_col))
if self.is_image(file_col):
im.save_file(this_request.files[file_col], getattr(item, file_col))
