def format_stack_frame(stack_frame, project: 'projects.Project'):...
"""docstring"""
filename = stack_frame.filename
if filename.startswith(project.source_directory):
filename = filename[len(project.source_directory) + 1:]
location = stack_frame.name
if location == '<module>':
location = None
return dict(filename=filename, location=location, line_number=stack_frame.
    lineno, line=stack_frame.line)
