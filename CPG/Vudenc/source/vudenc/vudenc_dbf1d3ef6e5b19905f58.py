import argparse, ast, json, sys, keyword, math
global_whitelist = ['__doc__', '__package__']
builtins_whitelist = ['abs', 'all', 'any', 'ArithmeticError', 'ascii',
    'AssertionError', 'AttributeError', 'BaseException', 'bin',
    'BlockingIOError', 'bool', 'BrokenPipeError', 'BufferError',
    '__build_class__', 'bytearray', 'bytes', 'BytesWarning', 'callable',
    'ChildProcessError', 'chr', 'classmethod', 'complex',
    'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
    'ConnectionResetError', 'delattr', 'DeprecationWarning', 'dict', 'dir',
    'divmod', '__doc__', 'Ellipsis', 'enumerate', 'EnvironmentError',
    'EOFError', 'Exception', 'False', 'FileExistsError',
    'FileNotFoundError', 'filter', 'float', 'FloatingPointError', 'format',
    'frozenset', 'FutureWarning', 'GeneratorExit', 'getatter', 'globals',
    'hasattr', 'hash', 'hex', 'id', 'ImportError', 'ImportWarning',
    'IndentationError', 'IndexError', 'input', 'int', 'InterruptedError',
    'IOError', 'IsADirectoryError', 'isinstance', 'issubclass', 'iter',
    'KeyboardInterrupt', 'KeyError', 'len', 'list', 'locals', 'LookupError',
    'map', 'max', 'MemoryError', 'memoryview', 'min', '__name__',
    'NameError', 'next', 'None', 'NotADirectoryError', 'NotImplemented',
    'NotImplementedError', 'object', 'oct', 'ord', 'OSError',
    'OverflowError', '__package__', 'PendingDeprecationWarning',
    'PermissionError', 'pow', 'print', 'ProcessLookupError', 'property',
    'range', 'RecursionError', 'ReferenceError', 'repr', 'ResourceWarning',
    'reversed', 'round', 'RuntimeError', 'RuntimeWarning', 'set', 'setattr',
    'slice', 'sorted', 'staticmethod', 'StopAsyncIteration',
    'StopIteration', 'str', 'sum', 'super', 'SyntaxError', 'SyntaxWarning',
    'SystemExit', 'TabError', 'TimeoutError', 'True', 'tuple', 'type',
    'TypeError', 'UnboundLocalError', 'UnicodeEncodeError',
    'UnicodeWarning', 'UserWarning', 'ValueError', 'vars', 'Warning',
    'ZeroDivisionError', 'zip']
def output_json(points, deductions):...
score = points - sum(d['points'] for d in deductions)
if score < 0:
score = 0
print(json.dumps({'score': score, 'deductions': deductions}))
def dock_points(deductions, points, reason):...
deductions.append({'points': points, 'reason': reason})
def fix_syntax_err(code, err):...
return None
