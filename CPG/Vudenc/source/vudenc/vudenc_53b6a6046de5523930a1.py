from DateTime.DateTime import DateTime
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Persistence import Persistent
from Acquisition import Implicit
import OFS.SimpleItem, OFS.ObjectManager
import zope.interface
import IZMSDaemon
__doc__ = 'ZMS product module.'
__version__ = '0.1'
__authorPermissions__ = ('manage_page_header', 'manage_page_footer',
    'manage_tabs', 'manage_main_iframe')
__viewPermissions__ = 'manage_menu',
__ac_permissions__ = ('ZMS Author', __authorPermissions__), ('View',
    __viewPermissions__)
manage = PageTemplateFile('zpt/object/manage', globals())
manage_workspace = PageTemplateFile('zpt/object/manage', globals())
manage_main = PageTemplateFile('zpt/ZMSObject/manage_main', globals())
manage_main_iframe = PageTemplateFile('zpt/ZMSObject/manage_main_iframe',
    globals())
def zmi_body_content(self, *args, **kwargs):...
request = self.REQUEST
response = request.RESPONSE
return self.getBodyContent(request)
