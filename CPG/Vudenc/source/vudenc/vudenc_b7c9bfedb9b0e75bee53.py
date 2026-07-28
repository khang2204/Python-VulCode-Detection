def write_extra_resources(self, compile_context):...
"""docstring"""
target = compile_context.target
if isinstance(target, ScalacPlugin):
self._write_scalac_plugin_info(compile_context.classes_dir, target)
if isinstance(target, JavacPlugin):
self._write_javac_plugin_info(compile_context.classes_dir, target)
if isinstance(target, AnnotationProcessor) and target.processors:
processor_info_file = os.path.join(compile_context.classes_dir,
    _PROCESSOR_INFO_FILE)
self._write_processor_info(processor_info_file, target.processors)
