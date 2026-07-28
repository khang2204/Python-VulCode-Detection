def is_cauldron_code(test_filename: str) ->bool:...
if not test_filename or not test_filename.startswith(cauldron_path):
return False
if test_filename.startswith(resources_path):
return False
return True
