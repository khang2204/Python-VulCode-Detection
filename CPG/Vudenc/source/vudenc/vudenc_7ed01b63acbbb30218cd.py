@classmethod...
if cls.count:
from beamr.interpreters import Config
package = Config.getRaw('verbatim')
packageList = Config.getRaw('vbtmCmds', 'packageNames')
if package not in packageList:
package = packageList[0]
Config.effectiveConfig['packages'].append(package)
Config.effectiveConfig['verbatim'] = package
cls.preambleDefs = Config.getRaw('vbtmCmds', 'once', package) + '\n'
for f in cls.todo:
if f.head:
cls.preambleDefs += Config.getRaw('vbtmCmds', 'foreach', package) % (f.
    insertCmd, f.head, f.body)
cls.preambleDefs += Config.getRaw('vbtmCmds', 'foreachNoLang', package) % (f
    .insertCmd, f.body)
