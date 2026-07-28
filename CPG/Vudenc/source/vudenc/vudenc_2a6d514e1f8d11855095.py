def _process_corrected(self, output, filename, file):...
"""docstring"""
for diff in self.__yield_diffs(file, output):
yield Result(self, self.diff_message, affected_code=(diff.range(filename),),
    diffs={filename: diff}, severity=self.diff_severity)
