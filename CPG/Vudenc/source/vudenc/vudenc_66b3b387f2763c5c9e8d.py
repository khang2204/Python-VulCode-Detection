from .app import Static
from ..app.templating import TemplateRoute
from ..gallery.pager import Pager
"""
    Main page
    """
path = '/'
template_name = 'main.mako'
@property...
return int(self.request.query['page'])
return 1
def get(self):...
index = self.config['runtime.gallery']
pager = Pager(index, self.current_page)
return {'pager': pager}
