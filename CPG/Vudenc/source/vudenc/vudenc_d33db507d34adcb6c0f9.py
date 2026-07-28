def get_stack_frames():...
"""docstring"""
cauldron_path = environ.paths.package()
resources_path = environ.paths.resources()
frames = list(traceback.extract_tb(sys.exc_info()[-1])).copy()
def is_cauldron_code(test_filename: str) ->bool:...
if not test_filename or not test_filename.startswith(cauldron_path):
return False
if test_filename.startswith(resources_path):
return False
return True
