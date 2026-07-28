def _WriteTemplate(self, template):...
contents = self._Read(os.path.join('tools', 'md_browser', template),
    relative_to=SRC_DIR)
self.wfile.write(contents.encode('utf-8'))
