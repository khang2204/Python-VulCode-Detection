def _render_template(self, request, error_msg=None):...
site = LoginWebSite(error_msg=error_msg, disclaimer_banner_file=self.
    _disclaimer_banner)
return renderElement(request, site)
