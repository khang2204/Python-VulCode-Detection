def format_error_message(exception_message, task_exception=False):...
"""docstring"""
lines = exception_message.split('\n')
if task_exception:
lines = lines[0:1] + lines[3:]
return '\n'.join(lines)
