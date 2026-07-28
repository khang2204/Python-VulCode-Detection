@staticmethod...
for k in content:
if k in target and isinstance(content[k], dict) and isinstance(target[k], dict
Config.recursiveUpdate(target[k], content[k])
if k in target and isinstance(content[k], list) and isinstance(target[k], list
target[k] += content[k]
target[k] = content[k]
