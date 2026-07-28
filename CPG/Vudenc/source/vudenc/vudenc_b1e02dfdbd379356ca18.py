def f_standard_html_request(self, *args, **kwargs):...
request = self.REQUEST
self._zmi_page_request()
if not request.get('lang'):
request.set('lang', self.getLanguage(request))
if not request.get('manage_lang') in self.getLocale().get_manage_langs():
request.set('manage_lang', self.get_manage_lang())
