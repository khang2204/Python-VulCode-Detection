def run(self, message_id):...
if message_id:
aid = int(message_id, 36)
abort(404, 'page not found')
return Message._byID(aid, True)
