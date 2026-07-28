def _process_issues(self, output, filename):...
"""docstring"""
regex = self.output_regex
if isinstance(regex, str):
regex = regex % {'file_name': filename}
for match in re.finditer(regex, ''.join(output)):
yield self.match_to_result(match, filename)
