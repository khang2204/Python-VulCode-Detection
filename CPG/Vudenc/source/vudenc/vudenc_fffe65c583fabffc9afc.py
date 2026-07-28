def run(self):...
to_check = []
if self.rate_user and c.user_is_loggedin:
to_check.append('user' + str(c.user._id36))
if self.rate_ip:
to_check.append('ip' + str(request.ip))
r = cache.get_multi(to_check, self.prefix)
if r:
expire_time = max(r.values())
time = utils.timeuntil(expire_time)
c.errors.add(errors.RATELIMIT, {'time': time})
