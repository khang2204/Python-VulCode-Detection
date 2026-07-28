def write_data(self, message):...
"""docstring"""
message_str = json.dumps(message)
message_str = json.dumps(fix_unicode_dict(message))
if len(self.events_requests) == 0:
return
[request.write(message_str + '\n') for request in self.events_requests]
