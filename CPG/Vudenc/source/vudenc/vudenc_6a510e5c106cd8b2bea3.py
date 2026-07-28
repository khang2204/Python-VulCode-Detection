def __init__(self, req, result_getter, event=None):...
super(AwaitableResponse, self).__init__(req['command'], event)
self.req = req
self._result_getter = result_getter
