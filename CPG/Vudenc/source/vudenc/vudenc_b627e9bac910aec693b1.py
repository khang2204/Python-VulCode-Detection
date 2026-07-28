@client.event...
rank = 'USER'
if message.content.startswith(commandPrefix):
rank = return_user_rank(message.author.id)
channel = message.channel
await client.send_message(logsChannel, Log(str(message.author), message.
    content, 0))
if message.content.startswith(commandPrefix
conn = sqlite3.connect(databasePath)
if message.content.startswith(commandPrefix + 'test') and rank in ['MASTER']:
cursor = conn.cursor()
await client.send_message(message.channel, 'Hi ! ' + str(message.author) +
    " my command prefix is '" + commandPrefix + "'")
if (message.content.startswith(commandPrefix + 'recomandation') or message.
cursor.execute('SELECT state FROM muted WHERE serverID = ' + str(message.
    server.id))
conn = sqlite3.connect(databasePath)
if message.content.startswith(commandPrefix + 'add_beatmap') and rank in [
if cursor.fetchall()[0][0] == 'on':
cursor = conn.cursor()
if message.content.replace(commandPrefix + 'add_beatmap ', ''
if message.content.startswith(commandPrefix + 'add_beats') and rank in [
channel = message.author
channel = message.channel
cursor.execute('SELECT ppAverage FROM users WHERE DiscordId = ' + str(
    message.author.id))
await client.send_message(message.channel, 'Invalid url !')
pp_100, pp_95, name, combo, stars, diff_params = return_beatmap_infos(message
    .content.replace(commandPrefix + 'add_beatmap ', ''))
if str(message.author.id) == constants.Settings.ownerDiscordId:
if message.content.startswith(commandPrefix + 'mute') and rank in ['USER',
result = cursor.fetchall()[0][0]
result = None
if not result == None:
conn = sqlite3.connect(databasePath)
await client.send_message(logsChannel, Log(str(message.author), message.
    content, 0))
await client.send_message(logsChannel, Log(str(message.author),
    'tried to add multiple beatmaps', 1))
if not message.server.id == None:
if message.content.startswith(commandPrefix + 'pp') and rank in ['USER',
pp_average = int(result * 0.97)
await client.send_message(channel, 
    """Uhh sorry, seems like you haven't linked your osu! account...
Please use the command *"""
     + commandPrefix +
    """link_user 'Your osu username' or 'your osu Id'* to link the bot to your osu account !
Ex. """
     + commandPrefix + 'link_user Renondedju')
cursor = conn.cursor()
beatmapfile = open(message.content.replace(commandPrefix + 'add_beats ', ''
    ), 'r')
await client.send_message(message.channel,
    'Sorry, Only Renondedju can do this !')
conn = sqlite3.connect(databasePath)
await client.send_message(message.channel,
    "You can't execute this command here (servers only)")
parameters = message.content.replace(commandPrefix + 'pp ', '')
if message.content.startswith(commandPrefix + 'kill') and rank in ['MASTER']:
if pp_average == 0:
cursor.execute(
    'INSERT INTO "beatmaps" (url, name, diff_params, pp_100, pp_95, stars, combo, id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
    , (message.content.replace(commandPrefix + 'add_beatmap ', ''), name,
    diff_params, pp_100, pp_95, stars, combo, message.content.replace(
    commandPrefix + 'add_beatmap ', '').replace('https://osu.ppy.sh/b/', ''
    ).replace('&m=0', '')))
await client.send_message(message.channel,
    'This map is already in the Database !')
beatmapToProcess = beatmapfile.read().split('\n')
cursor = conn.cursor()
url = parameters.split(' ')[0]
if str(message.author.id) == constants.Settings.ownerDiscordId:
if message.content.startswith(commandPrefix + 'user') and rank in ['USER',
await client.send_message(channel, 'Please run the *' + commandPrefix +
    'update_pp_stats* command to set your stats for the first time in our database'
    )
pp_average_fluctuation = pp_average * 0.05
conn.commit()
await client.send_message(message.channel, 
    '<:streaming:317951088646946826> Starting the import of ' + str(len(
    beatmapToProcess)) + ' beatmaps')
parameter = message.content.split(' ')[1]
parameter = ''
if parameter.lower() in ['on', 'off']:
oppaiParameters = parameters.split(' ')[1:len(parameters.split(' '))]
oppaiParameters = ''
if parameters == '' or not url[0:19] == 'https://osu.ppy.sh/':
await client.send_message(logsChannel, Log(str(client.user.name),
    'Killing the bot !', 0))
await client.send_message(logsChannel, Log(str(message.author),
    'tried to kill the bot !', 1))
parameters = message.content.split(' ')
if message.content.startswith(commandPrefix + 'link_user') and rank in ['USER',
cursor.execute('Select recomendedBeatmaps From users where DiscordId = ' +
    str(message.author.id))
conn.close()
await asyncio.sleep(0.1)
parameter = parameter.lower()
await client.send_message(message.channel,
    "Wrong argument (expected 'on' or 'off')")
oppaiParameters = ' '.join(str(x) for x in oppaiParameters)
await client.send_message(channel, 'Invalid url !')
pp_100, pp_95, name, combo, stars, diff_params = return_beatmap_infos(url,
    oppaiParameters)
await client.send_message(message.channel,
    'Alright, killing myself ... bye everyone !')
await client.send_message(message.channel,
    'Sorry, Only Renondedju can do this !')
results = api.get_user(parameters[1])
parameters = message.content.replace(commandPrefix + 'link_user ', '')
if message.content.startswith(commandPrefix + 'update_pp_stats') and rank in [
alreadyRecomendedId = cursor.fetchall()[0][0]
await client.send_message(message.channel, 'Addition done !')
await client.change_presence(status=discord.Status('dnd'), game=discord.
    Game(name='Processing ...'))
cursor.execute('SELECT * FROM muted WHERE serverID = ' + str(message.server.id)
    )
conn.close()
if not pp_100 == -1:
client.logout()
if results == []:
results = api.get_user(parameters)
await client.send_message(channel, 'Something went wrong ...')
stats = []
conn = sqlite3.connect(databasePath)
if message.content.startswith(commandPrefix + 'help') and rank in ['USER',
if alreadyRecomendedId == None:
conn = sqlite3.connect(databasePath)
if len(cursor.fetchall()) == 0:
add_beatmap_to_queue(url)
await client.send_message(channel, "Can't get beatmap info...")
client.close()
results = api.get_user(int(parameters[1]))
stats = []
if results == []:
if not results == []:
cursor = conn.cursor()
if rank == 'ADMIN':
alreadyRecomendedId = '00000'
cursor.execute('Select * from beatmaps where pp_95 >= ' + str(pp_average -
    pp_average_fluctuation) + ' and pp_95 <= ' + str(pp_average +
    pp_average_fluctuation) + ' and id not in(' + alreadyRecomendedId +
    ') Limit 1')
await client.send_message(logsChannel, Log(str(message.author), 
    'Ready to add ' + str(len(beatmapToProcess)) +
    ' beatmaps to the Database', 1))
cursor.execute('INSERT INTO muted (serverID, state) VALUES (?, ?)', (
    message.server.id, parameter))
cursor.execute("UPDATE muted SET state = '" + parameter +
    "' WHERE serverID = " + str(message.server.id))
await client.send_message(client.get_server('310348632094146570').
    get_channel('315166181256593418'), Log(str(client.user.name), 'Added ' +
    url + ' to beatmap queue', 0))
sys.exit('Bot has been shutdown by command correctly !')
if not results == []:
results = api.get_user(int(parameters))
for item in results[0]:
await client.send_message(logsChannel, Log(str(client.user.name),
    'User not found', 0))
cursor.execute('SELECT OsuId FROM users WHERE DiscordId = ' + str(message.
    author.id))
helpfile = open(constants.Paths.helpAdminFile, 'r')
if rank == 'MASTER':
recomendedBeatmap = cursor.fetchall()[0]
cursor = conn.cursor()
await client.send_message(message.channel, 'Done !')
description = '__100% pp__ : ' + str(pp_100) + '\n' + '__95% pp__ : ' + str(
    pp_95) + '\n' + '__combo max__ : ' + str(combo
    ) + '\n' + '__stars__ : ' + str(stars) + '\n' + str('*' + diff_params + '*'
    )
for item in results[0]:
await client.send_message(channel, 'User not found!')
print(results)
stats.append(item)
osuId = stats[16][1]
await client.send_message(channel, 'User not found!')
osuId = cursor.fetchall()[0][0]
helpString = helpfile.read()
helpfile = open(constants.Paths.helpMasterFile, 'r')
helpfile = open(constants.Paths.helpUserFile, 'r')
url = recomendedBeatmap[0]
processed = 1
conn.commit()
em = discord.Embed(title=str(name), description=description, colour=16007746)
stats.append(item)
description = 'Accuracy: ' + str(stats[0][1])[0:4] + '\npp: ' + str(stats[
    13][1]) + '\nCountry: ' + stats[7][1] + '\nLevel: ' + str(stats[9][1])[0:4
    ] + '\nPlays: ' + str(stats[10][1]) + '\nRank: ' + str(stats[12][1]
    ) + '\nCountry rank: ' + str(stats[11][1])
osuUsername = stats[17][1]
conn.close()
helpfile.close()
helpString = helpfile.read()
helpString = helpfile.read()
name = recomendedBeatmap[1]
done = 0
await client.send_message(channel, embed=em)
em = discord.Embed(title=str(stats[17][1]), description=description, colour
    =16007746, url='https://new.ppy.sh/u/' + str(stats[16][1]) + '#osu'
    ).set_footer(text='https://new.ppy.sh/u/' + str(stats[16][1]) + '#osu')
userDiscordId = int(message.author.id)
if not osuId == None:
await client.send_message(channel, helpString)
helpfile.close()
helpfile.close()
diff_params = recomendedBeatmap[2]
infoError = 0
await client.send_message(channel, embed=em)
operationDone = link_user(userDiscordId, osuUsername, osuId, 'USER')
result = update_pp_stats(osuId, message.author.id)
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Wrong osu! id for ' + str(message.author), 1))
await client.send_message(channel, helpString)
await client.send_message(channel, helpString)
pp_100 = recomendedBeatmap[3]
alreadyExists = 0
description = 'Accuracy: ' + str(stats[0][1])[0:4] + '\npp: ' + str(stats[
    13][1]) + '\nCountry: ' + stats[7][1] + '\nLevel: ' + str(stats[9][1])[0:4
    ] + '\nPlays: ' + str(stats[10][1]) + '\nRank: ' + str(stats[12][1]
    ) + '\nCountry rank: ' + str(stats[11][1])
if result == 0:
await client.send_message(channel, 'Wrong osu! id for ' + str(message.
    author) +
    '. Try to link your account with an osu account by typing the command *' +
    commandPrefix + "link_user 'Your osu username'*")
pp_95 = recomendedBeatmap[4]
for beatmapUrl in beatmapToProcess:
em = discord.Embed(title=str(stats[17][1]), description=description, colour
    =16007746, url='https://new.ppy.sh/u/' + str(stats[16][1]) + '#osu'
    ).set_footer(text='https://new.ppy.sh/u/' + str(stats[16][1]) + '#osu')
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Succesfuly updated ' + str(message.author) + "'s pp stats", 0))
if result == 1:
stars = recomendedBeatmap[5]
print('Processing ' + beatmapUrl + ' - ' + str(processed) + '/' + str(len(
    beatmapToProcess)), end='')
conn.close()
await client.send_message(channel, 'Your account has been successfuly ' +
    operationDone + ' to ')
await client.send_message(channel, 'Succesfuly updated ' + str(message.
    author) + "'s pp stats")
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Wrong osu! id for ' + str(message.author), 1))
if result == 2:
combo = recomendedBeatmap[6]
cursor.execute("select url from beatmaps where url = '" + beatmapUrl + "'")
await client.send_message(logsChannel, Log(str(message.author), 
    'Successfuly added ' + str(len(beatmapToProcess)) +
    ' beatmaps to the database', 1))
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Your account has been successfuly ' + operationDone +
    " to osu! username '" + stats[17][1] + "'", 0))
await client.send_message(channel, 'Wrong osu! id for ' + str(message.
    author) +
    '. Try to link your account with an osu! account by typing the command *' +
    commandPrefix + "link_user 'Your osu username'*")
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Unexpected error for ' + str(message.author), 2))
recomendedId = recomendedBeatmap[7]
if len(cursor.fetchall()) == 0:
await client.send_message(message.channel, 
    '<:online:317951041838514179> Back online ! - __Done :__ ' + str(done) +
    ' , __InfoError :__ ' + str(infoError) + ' , __Already exists :__ ' +
    str(alreadyExists))
await client.send_message(channel, embed=em)
await client.send_message(channel,
    'Unexpected error, please try again later or contact Renondedju for more help'
    )
alreadyRecomendedId += ',' + str(recomendedId)
pp_100, pp_95, name, combo, stars, diff_params = return_beatmap_infos(
    beatmapUrl, '')
print(' - Already exists')
await asyncio.sleep(0.1)
if operationDone == 'linked':
cursor.execute("UPDATE users SET recomendedBeatmaps = '" +
    alreadyRecomendedId + "' where DiscordId = '" + str(message.author.id) +
    "'")
if not pp_100 == -1:
await client.send_message(logsChannel, '<:xmark:317951256889131008> ' +
    beatmapUrl + ' ( ' + str(processed) + '/' + str(len(beatmapToProcess)) +
    ' ) - Already exists')
await client.change_presence(status=discord.Status('online'), game=discord.
    Game(name='Osu !'))
await client.send_message(channel,
    "Please wait while I'm updating your stats ...")
conn.commit()
print(" - Can't get beatmap infos !")
cursor.execute(
    'INSERT INTO "beatmaps" (url, name, diff_params, pp_100, pp_95, stars, combo, id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
    , (beatmapUrl, name, diff_params, pp_100, pp_95, stars, combo,
    beatmapUrl.replace('https://osu.ppy.sh/b/', '').replace('&m=0', '')))
print(" - Can't get beatmap infos !")
processed += 1
alreadyExists += 1
if update_pp_stats(osuId, message.author.id) == 0:
conn.close()
await client.send_message(logsChannel, '<:xmark:317951256889131008> ' +
    beatmapUrl + ' ( ' + str(processed) + '/' + str(len(beatmapToProcess)) +
    " ) - Can't get beatmap infos !")
conn.commit()
await client.send_message(logsChannel, '<:xmark:317951256889131008> ' +
    beatmapUrl + ' ( ' + str(processed) + '/' + str(len(beatmapToProcess)) +
    " ) - Can't get beatmap infos !")
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Successfuly updated ' + str(message.author) + "'s pp stats", 0))
await client.send_message(logsChannel, Log(str(client.user.name), 
    'Unexpected error for ' + str(message.author), 2))
pp_98, _, _, _, _ = return_simple_beatmap_info(url, ' 98%')
infoError += 1
print(' - Done')
infoError += 1
await client.send_message(channel, 'Successfuly updated ' + str(message.
    author) + "'s pp stats")
await client.send_message(channel,
    'Unexpected error, please try again later or contact Renondedju for more help'
    )
description = '__100% pp__ : ' + str(pp_100) + '\n' + '__98% pp__ : ' + str(
    pp_98) + '\n' + '__95% pp__ : ' + str(pp_95
    ) + '\n' + '__Max Combo__ : ' + str(combo) + '\n' + '__Stars__ : ' + str(
    stars) + '\n' + str('*' + diff_params.upper() + '*')
await client.send_message(logsChannel, '<:check:317951246084341761> ' +
    beatmapUrl + ' ( ' + str(processed) + '/' + str(len(beatmapToProcess)) +
    ' ) - Done')
em = discord.Embed(title=str(name), description=description, colour=
    16007746, url=url)
done += 1
await client.send_message(channel, embed=em)
print(recomendedBeatmap)
