def process_output(self, output, filename, file):...
"""docstring"""
if self.gives_corrected:
return self._process_corrected(output, filename, file)
return self._process_issues(output, filename)
