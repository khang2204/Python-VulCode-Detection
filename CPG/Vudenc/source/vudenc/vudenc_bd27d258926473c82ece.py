def __init__(self, txt):...
if txt.find('\t') > -1:
txt = txt.replace('\t', '    ')
super(Document, self).__init__(docParser.parse(txt, docLexer), after=self.end)
warn(
    "Input file has tabs, which will be considered 4 spaces; but please don't use tabs!"
    )
Config.resolve()
debug('Final config', Config.effectiveConfig)
ListItem.resolve(self.children)
Column.resolve(self.children)
VerbatimEnv.resolve()
packageDef = self.splitCmd(self.docClassCmd, Config.getRaw('docclass'))
for pkg in Config.effectiveConfig['packages']:
packageDef += self.splitCmd(self.packageCmd, pkg)
packageDef += '\n'
outerPreamble = ''
for k in self.preambleCmds:
if k in Config.effectiveConfig:
innerPreamble = VerbatimEnv.preambleDefs
outerPreamble += self.preambleCmds[k] % Config.getRaw(k)
if Config.effectiveConfig.get('titlepage', 'no') in ['yes', 'y', 'true', True]:
innerPreamble += self.titlePageCmd
self.before = packageDef + outerPreamble + self.begin + innerPreamble
