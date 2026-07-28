def match(msg):...
if msg.type != 'response':
return False
result['msg'] = msg
return msg.request_seq == seq
