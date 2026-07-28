@classmethod...
ret = []
for plugin, args in javac_plugin_map.items():
for arg in args:
return ret
if ' ' in arg:
ret.append('-Xplugin:{} {}'.format(plugin, ' '.join(args)))
