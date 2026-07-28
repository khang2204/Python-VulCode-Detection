def register_extra_products_from_contexts(self, targets, compile_contexts):...
compile_contexts = [self.select_runtime_context(compile_contexts[t]) for t in
    targets]
zinc_analysis = self.context.products.get_data('zinc_analysis')
zinc_args = self.context.products.get_data('zinc_args')
if zinc_analysis is not None:
for compile_context in compile_contexts:
if zinc_args is not None:
zinc_analysis[compile_context.target] = (compile_context.classes_dir,
    compile_context.jar_file, compile_context.analysis_file)
for compile_context in compile_contexts:
args = fp.read().split()
zinc_args[compile_context.target] = args
