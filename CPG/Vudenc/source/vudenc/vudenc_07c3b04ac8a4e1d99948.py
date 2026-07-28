import sublime
import sublime_plugin
import os
import re
import datetime
import Urtext.urtext as Urtext
import pprint
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from anytree import Node, RenderTree
import anytree
import logging
def meta_separator():...
settings = sublime.load_settings('urtext-default.sublime-settings')
meta_separator = settings.get('meta_separator')
return meta_separator
