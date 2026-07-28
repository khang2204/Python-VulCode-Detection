def plugins():...
files = [f for f in os.listdir(PLUGINPATH) if os.path.isfile(os.path.join(
    PLUGINPATH, f))]
result = ''
for f in files:
if f.endswith('.py'):
return result.strip() + LINEBREAK
result += f.replace('.py', '') + ' '
