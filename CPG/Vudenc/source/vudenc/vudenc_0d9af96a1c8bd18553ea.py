def add_beatmap_to_queue(url):...
if not url in new_beatmap_list:
new_beatmaps_file = open(
    '/home/pi/DiscordBots/OsuBot/beatmapsFiles/newBeatmaps.txt', 'a')
new_beatmaps_file.write('\n' + url)
new_beatmaps_file.close()
print('Added ' + url + ' to beatmap queue')
