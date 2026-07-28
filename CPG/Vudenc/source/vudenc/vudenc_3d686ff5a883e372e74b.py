def _is_newer(self, header_source, hostname):...
if not hostname:
output_path = self.output_path(self.create_filename(hostname))
old_header = Header.parse(output_path)
return header_source.is_newer_than(old_header)
