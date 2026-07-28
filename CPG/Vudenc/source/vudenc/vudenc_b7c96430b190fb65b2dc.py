def __init__(self):...
self._logger = logging.getLogger(self.__class__.__name__)
self.observers = []
self.observerscache = {}
self.observertimers = {}
self.observerLock = threading.Lock()
