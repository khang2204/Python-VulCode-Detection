async def save(self, *args, **kwargs):...
content = kwargs.pop('content', None)
if content is not None:
await self.set_content(content)
return await super().save(*args, **kwargs)
