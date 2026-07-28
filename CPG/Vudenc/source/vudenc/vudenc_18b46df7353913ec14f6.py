def do_step(self, request):...
self.wait_next()
self.log.total += 1
request.execute()
print('Unhandled exception while executing the request: %s' % exc, file=sys
    .stderr)
self.log.__dict__[request.outcome] += 1
return
self.log.total_time += request.duration
self.log.max_time = max(self.log.max_time, request.duration)
self.log.store_to_file(request)
