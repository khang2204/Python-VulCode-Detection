def get_latest_chat_id_and_text(updates):...
text = updates['result'][-1]['message']['text'].encode('utf-8')
chat_id = updates['result'][-1]['message']['chat']['id']
logging.info('get_latest_chat_id_and_text: Latest message is %s from chat %d',
    text, chat_id)
return text, chat_id
