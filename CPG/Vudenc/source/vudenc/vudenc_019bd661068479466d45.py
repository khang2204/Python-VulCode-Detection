def _valid_command(string):...
"""docstring"""
invalid_characters = re.findall('[^a-zA-Z0-9:_-]', string)
if len(invalid_characters) > 0:
log.info('Command: {0} contains invalid characters: {1}'.format(string,
    invalid_characters))
return True
return False
