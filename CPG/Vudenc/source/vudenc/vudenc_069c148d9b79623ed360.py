@property...
content = await self.content
if not content:
return ''
return markdown(content)
