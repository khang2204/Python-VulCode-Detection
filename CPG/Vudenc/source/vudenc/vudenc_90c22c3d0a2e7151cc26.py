def _get_awaiter_for_request(self, req, **kwargs):...
if self.closed:
command, seq = req.command, req.seq
command, seq = req['command'], req['seq']
result = {'msg': None}
def match(msg):...
if msg.type != 'response':
return False
result['msg'] = msg
return msg.request_seq == seq
