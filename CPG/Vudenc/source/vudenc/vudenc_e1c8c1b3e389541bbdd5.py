def _zmi_page_request(self, *args, **kwargs):...
for daemon in filter(lambda x: IZMSDaemon.IZMSDaemon in list(zope.interface
daemon.startDaemon()
request = self.REQUEST
request.set('ZMS_THIS', self.getSelf())
request.set('ZMS_DOCELMNT', self.breadcrumbs_obj_path()[0])
request.set('ZMS_ROOT', request['ZMS_DOCELMNT'].absolute_url())
request.set('ZMS_COMMON', getattr(self, 'common', self.getHome()).
    absolute_url())
request.set('ZMI_TIME', DateTime().timeTime())
request.set('ZMS_CHARSET', request.get('ZMS_CHARSET', 'utf-8'))
if not request.get('HTTP_ACCEPT_CHARSET'):
request.set('HTTP_ACCEPT_CHARSET', '%s;q=0.7,*;q=0.7' % request['ZMS_CHARSET'])
if (request.get('ZMS_PATHCROPPING', False) or self.getConfProperty(
base = request.get('BASE0', '')
if request['ZMS_ROOT'].startswith(base):
request.set('ZMS_ROOT', request['ZMS_ROOT'][len(base):])
request.set('ZMS_COMMON', request['ZMS_COMMON'][len(base):])
