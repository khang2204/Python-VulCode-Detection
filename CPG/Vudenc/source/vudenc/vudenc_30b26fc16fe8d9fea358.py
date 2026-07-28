def __init__(self, url, logger, service, behavior=cbehavior.available,...
self.url = url
self.service = service
self.behavior = behavior
self.settings = settings
self.logger = logger.bind(context=type(self).__name__, url=url)
self.handler = handler or []
self.warcinfo = warcinfo
