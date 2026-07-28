def get_contents(self, host, path):...
parsed_path = Path(path)
if host == 'localhost':
contents = self.local_listing(parsed_path)
contents = self.remote_listing(host, parsed_path)
return contents
