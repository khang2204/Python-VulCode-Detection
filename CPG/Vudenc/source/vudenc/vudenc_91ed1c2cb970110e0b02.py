def return_simple_beatmap_info(url, oppaiParameters):...
url = url.replace('/b/', '/osu/').split('&', 1)[0]
if oppaiParameters == '':
command = 'curl ' + url + ' | /home/pi/DiscordBots/Oppai/oppai/oppai -'
command = ('curl ' + url + ' | /home/pi/DiscordBots/Oppai/oppai/oppai - ' +
    oppaiParameters)
return get_infos(subprocess.Popen(command, stdout=subprocess.PIPE, stderr=
    subprocess.STDOUT, shell=True).stdout.read())
