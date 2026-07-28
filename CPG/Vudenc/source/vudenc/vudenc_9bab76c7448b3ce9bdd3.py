def setup(bot):...
from os import path
if not path.exists('./data/ed.db'):
from to_sqlalchemy import update
bot.add_cog(EDDB(bot))
update()
