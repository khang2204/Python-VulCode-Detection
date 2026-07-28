def concretize_iofile(f, wildcards):...
if not isinstance(f, _IOFile):
return IOFile(f, rule=self)
return f.apply_wildcards(wildcards, fill_missing=f in self.dynamic_input,
    fail_dynamic=self.dynamic_output)
