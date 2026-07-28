def post(self):...
cfgDAO.persistConfig(self.get_argument('AudioCodec'), self.get_argument(
    'AudioRate'), self.get_argument('VideoCodec'), self.get_argument(
    'VideoRate'), self.get_argument('VideoSize'), self.get_argument(
    'StreamEncryption'), self.get_argument('GenEncryptionKey'))
self.render('../config.html', cfg=cfgDAO.loadConfig())
