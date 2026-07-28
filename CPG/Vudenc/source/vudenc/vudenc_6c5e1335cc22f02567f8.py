def do_verbose_log(self, content):...
"""docstring"""
content = log_remove_escapes(content)
content = log_encode_html(content)
fdesc.writeToFD(fd.fileno(), content + '\n')
log.err('Unable to open %s: %s' % (GLSetting.httplogfile, excep))
