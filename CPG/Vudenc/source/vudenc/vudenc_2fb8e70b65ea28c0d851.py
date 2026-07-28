from . import pathexpr
from . import attrexpr
from . import ugoexpr
from . import fs
import copy
import collections
import itertools
import os
import glob
"""

{
  
  'collections' : {
    },
    
  'globals' : {},
  
  'rules' : {
  
    'ROOT' : [
        ['multiple', { 
            'key' : 'department'
            'bookmarks' : ['workarea'],
            'localattributes' : {},
            'treeattributes' : {},
            'user' : '(parameter user)',
            'group' : 'vfx',
            'permissions' : 'rwxr-xr-x' 
         }],
        
        ['directory', {
           'name' : 'value'
         }]
      
      ],
    
    'alternative' : [
      ],
    
    'rule2' : [
      ]
    }
}

"""
"""
a rule is a list of directory levels.
a compiled rule has:
   a set of bookmarks under it
   a set of parameters under it
   a set of attributes under it

Directory level types:
  fixed : one or more fixed names, not parameterized
     fields : bookmarks, local attrs, tree attrs, name, user, group, permissions
  branch : redirects to one or more other rules, IN ORDER, no special attributes of its own
     fields: rules
  parameterized : any number of parameterized directories, there is one key and potentially many values.
     fields : bookmarks, local attrs, tree attrs, key, collection, user group, permissions
     if there is an collection attribute, then the values are restricted.
  regex : can represent zero or more parameters, as defined by the groups in the expression.  Also good when
     there is a prefix or suffix or restrictions on the character set.
     fields: bookmarks, local attrs, tree attrs, pattern, collections, user, group, permissions
     regex is TODO
"""
FnLevel = {}
def register_level(cls):...
FnLevel[cls.__name__] = cls()
return cls
