import asyncio
import sqlite3
import discord
from discord.ext import commands
import to_sqlalchemy
def __init__(self, bot):...
self.bot = bot
self.updating = False
@commands.group(aliases=['elite', 'ed'])...
"""docstring"""
if ctx.invoked_subcommand is None:
await ctx.send(
    f'Invalid command passed. Try "{self.bot.command_prefix[0]}help eddb"')
@eddb.command(aliases=['sys'])...
"""docstring"""
loop = asyncio.get_event_loop()
result = await loop.run_in_executor(None, self.system_search, inp)
await ctx.send(result)
def system_search(self, search):...
search = search.lower()
conn = sqlite3.connect('data/ed.db').cursor()
table = conn.execute(f"select * from populated where lower(name) = '{search}'")
results = table.fetchone()
if not results:
table = conn.execute(f"select * from systems where lower(name) = '{search}'")
if results:
results = table.fetchone()
keys = tuple(i[0] for i in table.description)
return 'No systems found.'
return '\n'.join(f"{key.replace('_', ' ').title()}: {field}" for key, field in
    zip(keys[1:], results[1:]) if field)
