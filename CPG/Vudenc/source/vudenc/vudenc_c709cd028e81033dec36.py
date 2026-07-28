def send_message(text, chat_id):...
text = urllib.parse.quote_plus(text)
url = '{}/sendMessage?text={}&chat_id={}&parse_mode=Markdown'.format(base_url,
    text, chat_id)
logging.info('send_message: Sending %s to chat %d', text, chat_id)
requests.get(url)
