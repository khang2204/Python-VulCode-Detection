def __init__(self, api_port):...
QNetworkAccessManager.__init__(self)
url = QUrl('http://localhost:%d/events' % api_port)
self.request = QNetworkRequest(url)
self.failed_attempts = 0
self.connect_timer = QTimer()
self.current_event_string = ''
self.tribler_version = 'Unknown'
self.reply = None
self.emitted_tribler_started = False
self.shutting_down = False
self._logger = logging.getLogger('TriblerGUI')
