@command...
"""docstring"""
self.state.set_project(int(args[0]))
self.prompt = prnt_str('~', '(', self.state.active_project.name, ')', '>',
    ' ', PURPLE, TURQ, PURPLE, TURQ, BLUE, ORANGE)
