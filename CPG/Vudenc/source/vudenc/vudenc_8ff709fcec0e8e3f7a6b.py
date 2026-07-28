def make_router_rep_msg(self, reqid, seqnum, status, answer):...
iden = self.iden_reqid_map.get_key(reqid)
if seqnum == 0:
self.iden_reqid_map.del_value(iden, reqid)
msg = list(iden)
msg.append(b'')
msg.extend(make_rep_msg(reqid, seqnum, status, answer))
return msg
