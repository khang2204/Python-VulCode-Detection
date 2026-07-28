@functools.wraps(f)...
"""docstring"""
if hasattr(request, 'interaction'):
principals = map(lambda pp: pp.principal.id, request.interaction.participations
    )
principals = []
if hasattr(self, 'logFile'):
line = '%s %s - %s "%s" %d %s "%s" "%s"\n' % (request.getClientIP(),
    principals, self._logDateTime, '%s %s %s' % (self._escape(request.
    method), self._escape(request.uri), self._escape(request.clientproto)),
    request.code, request.sentLength or '-', self._escape(request.getHeader
    ('referer') or '-'), self._escape(request.getHeader('user-agent') or '-'))
self.logFile.write(line)
