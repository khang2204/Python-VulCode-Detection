def format_commands(settings):...
"""docstring"""
for key in ['cmd', 'ack', 'enq']:
if key in settings:
return settings
value = settings[key]
if isinstance(value, str):
for placeholder, replacement in [('$CR', '\r'), ('$LF', '\n'), ('$ACK',
if placeholder in value:
settings[key] = value
value = value.replace(placeholder, replacement)
