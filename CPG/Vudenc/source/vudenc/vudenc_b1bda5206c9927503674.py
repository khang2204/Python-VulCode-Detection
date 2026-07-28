@classmethod...
to_set = {}
seconds = g.RATELIMIT * 60
if seconds <= 0:
return
expire_time = datetime.now(g.tz) + timedelta(seconds=seconds)
if rate_user and c.user_is_loggedin:
to_set['user' + str(c.user._id36)] = expire_time
if rate_ip:
to_set['ip' + str(request.ip)] = expire_time
cache.set_multi(to_set, prefix, time=seconds)
