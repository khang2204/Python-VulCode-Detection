from grokcore.component import Adapter, implements, baseclass
from grokcore.security import require
from zope.interface import Interface
def render(request):...
def render_recursive(request, depth):...
def rw_transaction(request):...
"""docstring"""
def resolve(path):...
"""docstring"""
implements(IHttpRestView)
baseclass()
require('rest')
__builtin_attributes__ = ['id', 'children']
def filter_attributes(self, request, data):...
"""docstring"""
attrs = request.args.get('attrs', [''])[0]
if attrs:
filtered_data = {}
return data
for a in (attrs.decode('utf-8').split(',') + self.__builtin_attributes__):
if a in data:
return filtered_data
filtered_data[a] = data[a]
