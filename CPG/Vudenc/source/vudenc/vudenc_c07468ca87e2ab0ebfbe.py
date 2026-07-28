from const import *
from model import *
from utils import *
import reveal
"""An admin page to delete person records."""
ignore_deactivation = True
repo_required = False
admin_required = True
def get(self):...
xsrf_tool = XsrfTool()
user = users.get_current_user()
self.render('admin_delete_record.html', id=self.env.domain + '/person.',
    xsrf_token=xsrf_tool.generate_token(user.user_id(), 'admin_delete_record'))
def post(self):...
xsrf_tool = XsrfTool()
user = users.get_current_user()
if not (self.params.xsrf_token and xsrf_tool.verify_token(self.params.
self.error(403)
action = 'delete', str(self.params.id)
return False
self.redirect('/delete', id=self.params.id, signature=reveal.sign(action))
