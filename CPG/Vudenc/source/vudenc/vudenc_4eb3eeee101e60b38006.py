async def ret(*args, **kwargs):...
if time.time() - cache[1] > cache_page.timeout:
cache[0] = await func(*args, **kwargs)
return cache[0]
cache[1] = time.time()
