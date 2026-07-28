def main():...
parser = argparse.ArgumentParser(description=
    'Grade student code against given test cases. Results will be written over stdout in JSON'
    )
parser.add_argument('-n', '--name', required=True, help=
    'The name of the function the student was supposed to implement')
parser.add_argument('-p', '--points', type=int, default=0, help=
    'The number of points this question is worth. This argument is only used when -c is passed, and defaults to 0'
    )
parser.add_argument('-c', '--code', help=
    "The student's code submission. Make sure to carefully escape this argument as a single string. If this argument is ommitted then this program just checks the validity of the test cases. The exit status indicates the validity of the cases"
    )
parser.add_argument('-t', '--test_case', required=True, action='append',
    help=
    "The test cases to run the students code against. Each test case must take the form of of a function call without the function name followed by a comparison to a return value. For example ``(1, 2) == 3'' or ``(1, 2, (3, 4), *[5, 6], last=8) == None''"
    )
parser.add_argument('-v', '--verbose', action='count', default=0, help=
    'Specifies verbositiy level. Each time this flag is specified, the count goes up by one. Level 1 or greater outputs additional information about exceptions that occur'
    )
args = parser.parse_args()
vlevel = args.verbose
name = args.name
if not name.isidentifier() or keyword.iskeyword(name):
test_case_objs = []
for i, test_case in enumerate(args.test_case):
test_case = name + test_case
code = args.code
expr = ast.parse(test_case, mode='eval')
if vlevel >= 1:
if not expr:
if not code:
print(repr(e), file=sys.stderr)
expr = None
valid = False
return
deductions = []
if type(expr) == ast.Expression:
tree = None
comp = expr.body
if not valid:
while not tree:
if type(comp) == ast.Compare and len(comp.ops) == len(comp.comparators) == 1:
obj = compile(expr, '<unknown>', 'eval')
if vlevel >= 1:
if not obj:
if not tree:
tree = ast.parse(code)
fixed = fix_syntax_err(code, se)
left = comp.left
print(repr(e), file=sys.stderr)
obj = None
test_case_objs.append(obj)
output_json(args.points, deductions)
valid = False
if not fixed:
right = comp.comparators[0]
return
if type(tree) == ast.Module and len(tree.body) == 1:
if vlevel >= 1:
code = fixed
left_valid = False
fdef = tree.body[0]
if not valid:
print(repr(se), file=sys.stderr)
dock_points(deductions, args.points, 'syntax error')
if vlevel >= 1:
if type(left) == ast.Call:
if type(fdef) in [ast.FunctionDef, ast.AsyncFunctionDef]:
dock_points(deductions, args.points, 'not just a single function definition')
code_obj = compile(tree, '<unknown>', 'exec')
if vlevel >= 1:
if not code_obj:
print(repr(e), file=sys.stderr)
dock_points(deductions, args.points, 'failed to parse code')
if type(left.func) == ast.Name and left.func.id == name:
if left_valid:
if fdef.name != name:
output_json(args.points, deductions)
print(repr(e), file=sys.stderr)
code_obj = None
dock_points(deductions, args.points, 'failed to compile code')
deductions += grade(code_obj, name, args.points, test_case_objs, vlevel)
left_valid = True
if type(right) in [ast.Num, ast.Str, ast.Bytes, ast.NameConstant, ast.Dict,
fdef.name = name
valid = True
return
output_json(args.points, deductions)
output_json(args.points, deductions)
valid = True
dock_points(deductions, 1, 'misnamed function')
return
