def __init__(self, banner):...
super(DisclaimerElement, self).__init__()
self._set_loader(banner)
self._banner_filename = banner or '_login_disclaimer_banner.html'
