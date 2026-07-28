"""
Created on 6 Feb 2018

@author: Teodor Gherasim Nistor
"""
import yaml
import subprocess
import os
import re
from beamr.debug import warn, err
userConfigPath = os.path.expanduser('~/.beamrrc')
userConfigTemplate = """---
# Beam configuration file. Please include user settings between the 3 dashes and the 3 dots.
editor: %s

...
"""
effectiveConfig = {'docclass': 'beamer', 'packages': ['utf8,inputenc',
    'T1,fontenc', 'pdfpages', 'upquote', 'normalem,ulem'], 'graphicspath':
    [], 'theme': 'Copenhagen', 'scheme': 'beaver', 'imgexts': ['', '.png',
    '.pdf', '.jpg', '.mps', '.jpeg', '.jbig2', '.jb2', '.PNG', '.PDF',
    '.JPG', '.JPEG', '.JBIG2', '.JB2'], 'safe': True, 'pdflatex':
    'pdflatex', 'verbatim': 'listings', 'vbtmCmds': {'packageNames': [
    'listings', 'minted'], 'once': {'listings':
    '\\definecolor{codegreen}{rgb}{0.1,0.4,0.1}\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\\definecolor{codepurple}{rgb}{0.4,0,0.7}\\lstdefinestyle{defostyle}{commentstyle=\\color{codegreen},keywordstyle=\\color{blue},numberstyle=\\tiny\\color{codegray},stringstyle=\\color{codepurple},basicstyle=\\footnotesize\\ttfamily,breakatwhitespace=false,breaklines=true,captionpos=b,keepspaces=true,numbers=left,numbersep=5pt,showspaces=false,showstringspaces=false,showtabs=false,tabsize=3}'
    , 'minted': ''}, 'foreach': {'minted':
    """\\defverbatim[colored]%s{
  \\begin{minted}[xleftmargin=20pt,linenos]{%s}
%s
  \\end{minted}
}
"""
    , 'listings':
    """\\defverbatim[colored]%s{
  \\begin{lstlisting}[language=%s,style=defostyle]
%s
  \\end{lstlisting}
}
"""
    }, 'foreachNoLang': {'minted':
    """\\defverbatim[colored]%s{
  \\begin{minted}[xleftmargin=20pt,linenos]{text}
%s
  \\end{minted}
}
"""
    , 'listings':
    """\\defverbatim[colored]%s{
  \\begin{lstlisting}[style=defostyle]
%s
  \\end{lstlisting}
}
"""
    }, 'insertion': '\\codeSnippet%s '}, 'emph': {'*': '\\textbf{%s}', '_':
    '\\textit{%s}', '~': '\\sout{%s}', '**': '\\alert{%s}', '__':
    '\\underline{%s}'}, 'stretch': {'<>': lambda s: 
    '\\centering\\noindent\\resizebox{0.9\\textwidth}{!}{%s}' % s, '><': lambda
    s: """\\begin{center}
%s
\\end{center}""" % s, '<<': lambda s: 
    """\\begin{flushleft}
%s
\\end{flushleft}""" % s, '>>': lambda s: 
    """\\begin{flushright}
%s
\\end{flushright}""" % s, '+': lambda s:
    '\\pause ', '>': lambda s: '\\hfill ', '^^': lambda s: '\\vspace{-%s}' %
    s, 'vv': lambda s: '\\vspace{%s}' % s, '__': lambda s: 
    '{\\footnotesize %s}' % s, ':': lambda s: ''}, 'bib': None}
docConfig = []
cmdlineConfig = {}
def __init__(self, txt):...
self.parsedConfig = yaml.load_all(txt)
self.__class__.docConfig.append(self)
@classmethod...
configStubs = [cls.cmdlineConfig]
while len(cls.docConfig):
for stub in cls.docConfig.pop(0).parsedConfig:
for stub in yaml.load_all(re.sub('(^|\\n\\.\\.\\.)[\\s\\S]*?($|\\n---)',
for c in reversed(configStubs):
configStubs.append(stub)
if stub:
cls.recursiveUpdate(cls.effectiveConfig, c)
@classmethod...
configStubs.append(stub)
cls.recursiveUpdate(cls.cmdlineConfig, yaml.load(general))
cls.recursiveUpdate(cls.cmdlineConfig, special)
@classmethod...
d = cls.effectiveConfig
warn('Could not get raw configuration for', arg, 'due to', repr(e))
@classmethod...
for i in range(len(arg)):
return None
d = cls.effectiveConfig
warn('Could not get configuration for', arg, 'due to', repr(e))
@classmethod...
d = d[arg[i]]
return d
for i in range(len(arg)):
return kw['default'] if 'default' in kw else lambda s: s
if not os.path.isfile(cls.userConfigPath):
d = d[arg[i]]
if callable(d):
if editor:
if not editor:
return d
return lambda s: d % s
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
