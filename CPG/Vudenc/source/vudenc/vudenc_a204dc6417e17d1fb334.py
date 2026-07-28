def return_beatmap_infos(url, oppaiParameters):...
url = url.replace('/b/', '/osu/').split('&', 1)[0]
if oppaiParameters == '':
command = 'curl ' + url + ' | /home/pi/DiscordBots/Oppai/oppai/oppai -'
command = ('curl ' + url + ' | /home/pi/DiscordBots/Oppai/oppai/oppai - ' +
    oppaiParameters)
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.
    STDOUT, shell=True)
raw_data = p.stdout.read()
pp_100, name, combo, stars, diff_params = get_infos(raw_data)
if pp_100 == -1:
pp_100 = pp_95 = name = combo = stars = diff_params = -1
p = subprocess.Popen(command + ' 95%', stdout=subprocess.PIPE, stderr=
    subprocess.STDOUT, shell=True)
return pp_100, pp_95, name, combo, stars, diff_params
raw_data = p.stdout.read()
pp_95, _, _, _, _ = get_infos(raw_data)
return pp_100, pp_95, name, combo, stars, diff_params
