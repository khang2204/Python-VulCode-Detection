def parse(self, response):...
url_parts = response.url.split('/')
if len(url_parts) == 5:
print('Mainpage')
print('Not Mainpage')
page_name = 'Main'
page_name = url_parts[len(url_parts) - 1]
profile_name = url_parts[len(url_parts) - 1]
profile_name = url_parts[len(url_parts) - 2]
websites = {'_id': profile_name, 'URL': response.url, page_name: response.
    body.decode('utf-8')}
yield {'websites': websites}
