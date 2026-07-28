def run(self, link_id):...
if link_id:
aid = int(link_id, 36)
if self.redirect:
return Link._byID(aid, True)
abort(404, 'page not found')
return None
