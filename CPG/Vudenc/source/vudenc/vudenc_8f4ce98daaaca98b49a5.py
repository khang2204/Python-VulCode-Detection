@staticmethod...
"""docstring"""
valid_jmessage = {}
for key in message_template.keys():
if key not in jmessage:
if GLSetting.loglevel == 'DEBUG':
log.err('key %s not in %s' % (key, jmessage))
valid_jmessage[key] = jmessage[key]
for double_k in jmessage.keys():
jmessage = valid_jmessage
if double_k not in message_template.keys():
for key, value in message_template.iteritems():
log.err('[!?] key %s not expected' % double_k)
if not BaseHandler.validate_type(jmessage[key], value):
for key, value in jmessage.iteritems():
if not BaseHandler.validate_type(value, message_template[key]):
return True
