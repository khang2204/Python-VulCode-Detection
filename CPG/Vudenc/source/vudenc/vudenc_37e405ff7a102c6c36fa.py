def run(self, cid):...
if cid:
cid = int(cid, 36)
return Comment._byID(cid, True)
