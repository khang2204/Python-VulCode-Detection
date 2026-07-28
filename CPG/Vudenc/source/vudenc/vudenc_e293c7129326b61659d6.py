@classmethod...
configStubs = [cls.cmdlineConfig]
while len(cls.docConfig):
for stub in cls.docConfig.pop(0).parsedConfig:
for stub in yaml.load_all(re.sub('(^|\\n\\.\\.\\.)[\\s\\S]*?($|\\n---)',
for c in reversed(configStubs):
configStubs.append(stub)
if stub:
cls.recursiveUpdate(cls.effectiveConfig, c)
configStubs.append(stub)
