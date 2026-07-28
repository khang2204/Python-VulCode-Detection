@eddb.command(aliases=['u', 'upd'])...
"""docstring"""
if not self.updating:
self.updating = True
await ctx.send('Database update still in progress.')
await ctx.send('Database update in progress...')
loop = asyncio.get_event_loop()
await loop.run_in_executor(None, to_sqlalchemy.remake)
await ctx.send('Database update complete.')
self.updating = False
