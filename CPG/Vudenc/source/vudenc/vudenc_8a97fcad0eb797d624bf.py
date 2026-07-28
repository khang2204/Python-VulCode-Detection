def __init__(self, services_factory, portal=None, disclaimer_banner=None):...
BaseResource.__init__(self, services_factory)
self._static_folder = _get_static_folder()
self._startup_folder = _get_startup_folder()
self._portal = portal
self._disclaimer_banner = disclaimer_banner
self.putChild('startup-assets', File(self._startup_folder))
