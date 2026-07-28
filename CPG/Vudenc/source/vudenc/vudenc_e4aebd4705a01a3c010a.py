def make_reqid(self):...
while True:
reqid = random.randint(1, 2 ** 64 - 1)
if not reqid in self.response_handlers:
return reqid
