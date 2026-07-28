def __str__(self):...
from beamr.interpreters.config import Config
if Config.effectiveConfig['bib']:
return '\\cite{' + self.txt + '}'
warn('Citations used but no bibliography file given.')
return ''
