def add_files(self, root, prefix=None):...
root = decode_if_byte_string(root, force_text=True)
root = root.rstrip(os.path.sep) + os.path.sep
prefix = decode_if_byte_string(prefix)
prefix = ensure_leading_trailing_slash(prefix)
if self.autorefresh:
self.directories.insert(0, (root, prefix))
if os.path.isdir(root):
self.update_files_dictionary(root, prefix)
warnings.warn(u'No directory at: {}'.format(root))
