def run(self, id_str):...
if not id_str:
return None
cids = [int(i, 36) for i in id_str.split(',')]
comments = Comment._byID(cids, data=True, return_dict=False)
return comments
