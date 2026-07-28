def _sanitize_log_msg(self, msg):...
"""docstring"""
reg = '(?P<var>(pass|key|secret|PASS|KEY|SECRET).*?=)(?P<value>.*?\\s)'
return re.sub(reg, '\\g<var>****** ', msg)
