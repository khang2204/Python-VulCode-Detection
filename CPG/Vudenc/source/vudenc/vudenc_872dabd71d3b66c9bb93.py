@command...
"""docstring"""
projects = wrapper.todoist.get_projects()
cli.print_listing(projects, 0)
return projects
