@classmethod...
if not os.path.isfile(cls.userConfigPath):
if editor:
if not editor:
cf.write(cls.userConfigTemplate % editor)
err('Editor not given. Cannot edit.')
for d in yaml.load_all(cf):
if not editor:
subprocess.call([editor, cls.userConfigPath])
return 2
if 'editor' in d:
err('Editor not given. Cannot edit.')
return 0
editor = d['editor']
return 3
