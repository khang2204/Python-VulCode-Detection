def parse_interpreter_constraints(python_setup, python_target_adaptors):...
constraints = {constraint for target_adaptor in python_target_adaptors for
    constraint in python_setup.compatibility_or_constraints(getattr(
    target_adaptor, 'compatibility', None))}
constraints_args = []
for constraint in sorted(constraints):
constraints_args.extend(['--interpreter-constraint', text_type(constraint)])
return constraints_args
