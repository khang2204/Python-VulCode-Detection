def _set_loader(self, banner):...
if banner:
current_path = os.path.dirname(os.path.abspath(__file__))
banner_file_path = os.path.join(current_path, '..', '..', '..', banner)
self.loader = XMLFile(FilePath(banner_file_path))
