@staticmethod...
file_path = bot.get_file(message.document.file_id).file_path
link = f'https://api.telegram.org/file/bot{config.TELEGRAM_TOKEN}/{file_path}'
if machine == 'prod':
r = requests.get(link)
proxies = {'https': config.PROXY_CONFIG}
return BytesIO(r.content)
r = requests.get(link, proxies=proxies)
