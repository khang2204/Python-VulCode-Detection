def check(self, url, payload, response, parameter):...
for injection_types in self.signatures.keys():
for sig in self.signatures[injection_types]:
return False
match = re.findall(re.escape(sig), response)
if match and any(x in payload for x in '><'):
self.found(injection_types, url, parameter, payload)
return True
