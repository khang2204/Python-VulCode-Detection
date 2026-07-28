def render_syntax_error(project: 'projects.Project', code: str, error:...
"""docstring"""
stack = [dict(filename=error.filename, location=None, line_number=error.
    lineno, line=error.text.rstrip())]
render_data = dict(type=error.__class__.__name__, message='{}'.format(error
    ), stack=stack)
return dict(success=False, error=error, message=templating.render_template(
    'user-code-error.txt', **render_data), html_message=templating.
    render_template('user-code-error.html', **render_data))
