def grade(code_obj, name, points, test_case_objs, vlevel=0):...
deductions = []
points_per_case = points // len(test_case_objs)
instr_globals = {k: globals()[k] for k in global_whitelist if k in globals()}
instr_globals['__name__'] = name
instr_globals['__builtins__'] = {k: __builtins__.__dict__[k] for k in
    builtins_whitelist if k in __builtins__.__dict__}
instr_locals = {}
exec(code_obj, instr_globals, instr_locals)
if vlevel >= 1:
for i, test_case_obj in enumerate(test_case_objs):
print(repr(e), file=sys.stderr)
dock_points(deductions, points, 'unable to execute function')
return deductions
result = eval(test_case_obj, instr_globals, instr_locals)
if vlevel >= 1:
return deductions
if not result:
print(repr(e), file=sys.stderr)
dock_points(deductions, points_per_case, 'exception during test case %d' % i)
dock_points(deductions, points_per_case, 'failed test case %d' % i)
