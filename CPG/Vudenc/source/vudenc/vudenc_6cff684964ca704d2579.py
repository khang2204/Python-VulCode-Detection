def srcdir(path):...
"""docstring"""
if not workflow.included_stack:
return None
return os.path.join(os.path.dirname(workflow.included_stack[-1]), path)
