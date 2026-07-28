def get_json_from_url(url):...
response = requests.get(url)
decoded_content = response.content.decode('utf-8')
logging.info('GET %s responded with %s', url, decoded_content)
return json.loads(decoded_content)
