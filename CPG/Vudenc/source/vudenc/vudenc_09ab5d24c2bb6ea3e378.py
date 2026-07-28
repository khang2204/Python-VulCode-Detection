from cmd import Cmd
import wrapper
from objects import Project
from color import prnt, prnt_str, VIOLET, PURPLE, ORANGE, TURQ, BLUE
from cli_helpers import arglen, inject, state, emptystate, restrict, command
from cli_helpers import CmdError
import cli_helpers as cli
from state import CLIState
def __init__(self, conf):...
super().__init__()
self.state = CLIState()
self.conf = conf
@command...
"""docstring"""
projects = wrapper.todoist.get_projects()
cli.print_listing(projects, 0)
return projects
