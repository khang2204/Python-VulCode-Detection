def run(self):...
if is_banned_IP(request.ip):
c.errors.add(errors.BANNED_IP)
return request.ip
