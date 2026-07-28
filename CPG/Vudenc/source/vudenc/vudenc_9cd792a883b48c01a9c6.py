def executer(self, *args):...
"""docstring"""
options = self.options
url = 'http://{host}:{port}/{path}'.format(host=options.host, port=options.
    port, path=COMMANDS[options.prog])
log.logger.error('Daemon not available: %s', e)
request = json.dumps(args[1:])
log.logger.exception(e)
log.logger.debug("""Request to %s:
%s""", url, request)
response = urllib2.urlopen(url, request)
for i in ijson.items(response, 'item'):
yield from_json(i)
