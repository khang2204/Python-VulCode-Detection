def render_error(project: 'projects.Project', error: Exception) ->dict:...
"""docstring"""
render_data = dict(type=error.__class__.__name__, message='{}'.format(error
    ), stack=[format_stack_frame(f, project) for f in get_stack_frames()])
return dict(success=False, error=error, message=templating.render_template(
    'user-code-error.txt', **render_data), html_message=templating.
    render_template('user-code-error.html', **render_data))
