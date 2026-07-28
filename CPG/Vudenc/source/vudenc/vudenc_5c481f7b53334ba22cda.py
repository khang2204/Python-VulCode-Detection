"""
Created on Sat May 20 22:39:26 2017

@author: Renondedju
"""
import discord
import asyncio
import sys
import subprocess
import sqlite3
import re
from datetime import datetime
from osuapi import OsuApi, ReqConnector
import requests
import constants
client = discord.Client()
commandPrefix = constants.Settings.commandPrefix
api = OsuApi(constants.Api.osuApiKey, connector=ReqConnector())
mainChannel = None
logsChannel = None
databasePath = constants.Paths.beatmapDatabase
def return_user_rank(discordId):...
if not discordId == constants.Settings.ownerDiscordId:
conn = sqlite3.connect(databasePath)
return 'MASTER'
cursor = conn.cursor()
cursor.execute('SELECT rank FROM users WHERE discordId = ' + str(discordId))
rank = cursor.fetchall()[0][0]
rank = 'USER'
print(rank)
conn.close()
if rank == '':
rank = 'USER'
return rank
