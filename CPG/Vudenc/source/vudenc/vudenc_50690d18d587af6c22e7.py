def _execute_hermetic_compile(self, cmd, ctx):...
input_snapshot = ctx.target.sources_snapshot(scheduler=self.context._scheduler)
output_files = tuple(os.path.relpath(f.path.replace('.java', '.class'), ctx
    .target.target_base) for f in input_snapshot.files if f.path.endswith(
    '.java'))
exec_process_request = ExecuteProcessRequest(argv=tuple(cmd), input_files=
    input_snapshot.directory_digest, output_files=output_files, description
    ='Compiling {} with javac'.format(ctx.target.address.spec))
exec_result = self.context.execute_process_synchronously(exec_process_request,
    'javac', (WorkUnitLabel.TASK, WorkUnitLabel.JVM))
classes_directory = ctx.classes_dir
self.context._scheduler.materialize_directories((DirectoryToMaterialize(
    text_type(classes_directory), exec_result.output_directory_digest),))
