@property...
rv = await self.get_props_by_key('content')
if rv:
return rv.decode('utf-8')
