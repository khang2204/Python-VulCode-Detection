@bot.command()...
"""docstring"""
command = ' '.join(map(str, args))
idsearch = 'id=([\\d])'
tiersearch = 'tier=([^\\s]+)'
creatorsearch = 'creator=([^\\s]+)'
idformat = ''
tierformat = ''
creatorformat = ''
if re.search(idsearch, command) is not None:
idmatch = re.search(idsearch, command).group(1)
if re.search(tiersearch, command) is not None:
idformat = 'AND id = {}'.format(idmatch)
tiermatch = re.search(tiersearch, command).group(1)
if re.search(creatorsearch, command) is not None:
tierformat = "AND tier = '{}'".format(tiermatch)
creatormatch = re.search(creatorsearch, command).group(1)
query = (
    """
    SELECT id, tier, creator, description FROM quests
    WHERE completed = 'f'
    {}
    {}
    {};
    """
    .format(idformat, tierformat, creatorformat))
creatorformat = "AND creator = '{}'".format(creatormatch)
query_return = pgsql.retrieve_quest_data(pg_connection, query)
tab = tt.Texttable()
headings = ['ID', 'TIER', 'CREATOR', 'DESCRIPTION']
tab.header(headings)
for x in range(0, len(query_return), 5):
for row in query_return[x:x + 5]:
tab.add_row(row)
s = tab.draw()
print(len(query_return))
await ctx.send('```' + s + '```')
tab.reset()
