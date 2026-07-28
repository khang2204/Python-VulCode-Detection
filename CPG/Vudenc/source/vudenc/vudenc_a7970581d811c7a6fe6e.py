@classmethod...
if version == 'custom':
return tool
return '{}_{}'.format(tool, version.replace('.', '_'))
