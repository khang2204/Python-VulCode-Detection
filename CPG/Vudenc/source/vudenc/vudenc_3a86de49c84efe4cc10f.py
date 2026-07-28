def get_path(window):...
"""docstring"""
if window.project_data():
path = window.project_data()['urtext_path']
path = '.'
return path
