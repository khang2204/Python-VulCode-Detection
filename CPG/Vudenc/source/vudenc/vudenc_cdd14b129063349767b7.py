def console_output(self, targets):...
if not self.get_options().transitive:
targets = self.context.target_roots
input_snapshots = tuple(target.sources_snapshot(scheduler=self.context.
    _scheduler) for target in targets)
input_files = {f.path for snapshot in input_snapshots for f in snapshot.files}
list_file = os.path.join(tmpdir, 'input_files_list')
for input_file in sorted(input_files):
list_file_out.write(input_file)
list_file_snapshot = self.context._scheduler.capture_snapshots((
    PathGlobsAndRoot(PathGlobs(('input_files_list',)), text_type(tmpdir)),))[0]
list_file_out.write('\n')
cloc_path, cloc_snapshot = ClocBinary.global_instance().hackily_snapshot(self
    .context)
directory_digest = self.context._scheduler.merge_directories(tuple(s.
    directory_digest for s in input_snapshots + (cloc_snapshot,
    list_file_snapshot)))
cmd = ('/usr/bin/perl', cloc_path, '--skip-uniqueness', '--ignored=ignored',
    '--list-file=input_files_list', '--report-file=report')
req = ExecuteProcessRequest(argv=cmd, input_files=directory_digest,
    output_files=('ignored', 'report'), description='cloc')
exec_result = self.context.execute_process_synchronously(req, 'cloc', (
    WorkUnitLabel.TOOL,))
files_content_tuple = self.context._scheduler.product_request(FilesContent,
    [exec_result.output_directory_digest])[0].dependencies
files_content = {fc.path: fc.content.decode('utf-8') for fc in
    files_content_tuple}
for line in files_content['report'].split('\n'):
yield line
if self.get_options().ignored:
yield 'Ignored the following files:'
for line in files_content['ignored'].split('\n'):
yield line
