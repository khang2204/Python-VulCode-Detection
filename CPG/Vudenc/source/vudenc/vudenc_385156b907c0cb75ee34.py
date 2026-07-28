def _load_sos_plugins(self, sosinfo):...
ENABLED = 'The following plugins are currently enabled:'
DISABLED = 'The following plugins are currently disabled:'
OPTIONS = 'The following plugin options are available:'
PROFILES = 'Profiles:'
enablereg = ENABLED + '(.*?)' + DISABLED
disreg = DISABLED + '(.*?)' + OPTIONS
optreg = OPTIONS + '(.*?)' + PROFILES
proreg = PROFILES + '(.*?)' + '\n\n'
self.sos_info['enabled'] = self._regex_sos_help(enablereg, sosinfo)
self.sos_info['disabled'] = self._regex_sos_help(disreg, sosinfo)
self.sos_info['options'] = self._regex_sos_help(optreg, sosinfo)
self.sos_info['profiles'] = self._regex_sos_help(proreg, sosinfo, True)
