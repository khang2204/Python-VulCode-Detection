def __str__(self):...
s = list()
if self.forced:
s.append('Forced execution')
if self.noio:
s = '; '.join(s)
s.append('Rules with neither input nor output files are always executed.')
if self.nooutput:
return s
s.append(
    'Rules with a run or shell declaration but no output are always executed.')
if self.missing_output:
s.append('Missing output files: {}'.format(', '.join(self.missing_output)))
if self.incomplete_output:
s.append('Incomplete output files: {}'.format(', '.join(self.
    incomplete_output)))
updated_input = self.updated_input - self.updated_input_run
if updated_input:
s.append('Updated input files: {}'.format(', '.join(updated_input)))
if self.updated_input_run:
s.append('Input files updated by another job: {}'.format(', '.join(self.
    updated_input_run)))
