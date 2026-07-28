async def activity_update_loop(self):...
"""docstring"""
while True:
await self.next_activity()
await asyncio.sleep(20)
