import os
import sys
import threading
import traceback
import types
from importlib.abc import InspectLoader
from cauldron import environ
from cauldron import templating
from cauldron.cli import threads
from cauldron.runner import redirection
from cauldron.session import projects
def set_executing(on: bool):...
"""docstring"""
my_thread = threading.current_thread()
if isinstance(my_thread, threads.CauldronThread):
my_thread.is_executing = on
def run(project: 'projects.Project', step: 'projects.ProjectStep') ->dict:...
"""docstring"""
module_name = step.definition.name.rsplit('.', 1)[0]
module = types.ModuleType(module_name)
source_code = f.read()
code = InspectLoader.source_to_code(source_code, step.source_path)
return render_syntax_error(project, source_code, error)
setattr(module, '__file__', step.source_path)
setattr(module, '__package__', '.'.join([project.id.replace('.', '-')] +
    step.filename.rsplit('.', 1)[0].split(os.sep)))
def exec_test():...
step.test_locals = dict()
step.test_locals.update(module.__dict__)
exec(code, step.test_locals)
set_executing(True)
out = {'success': False}
set_executing(False)
threads.abort_thread()
out = None
return {'success': True} if out is None else out
if environ.modes.has(environ.modes.TESTING):
out = render_error(project, error)
exec_test()
exec(code, module.__dict__)
out = None
