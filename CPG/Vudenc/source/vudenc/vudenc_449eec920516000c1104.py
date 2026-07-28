def serialize(self):...
lines = []
time_string = strftime('%Y-%m-%d %H:%M:%S', localtime())
lines.append('%s on %s' % (Header.MON_CONF_GEN_COMMENT, time_string))
if self.etag:
lines.append('%s%s' % (Header.ETAG_COMMENT, self.etag))
if self.mtime:
lines.append('%s%d' % (Header.MTIME_COMMMENT, self.mtime))
return lines
