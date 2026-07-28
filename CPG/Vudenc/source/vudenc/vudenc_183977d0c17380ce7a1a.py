import scrapy
import json
from scrapers.scrapy_couchcrawl.helpers.profileLinkExtractor import KeyExtractor
name = 'fetch_profiles'
login_url = 'https://www.couchsurfing.com/users/sign_in'
login_user = 'q1686061@mvrht.net'
login_password = '3R3fk*CP'
login_data = {'user[login]': login_user, 'user[password]': login_password}
custom_settings = {'ITEM_PIPELINES': {
    'scrapy_couchcrawl.pipelines.ProfilesPipeline': 400},
    'AUTOTHROTTLE_ENABLED': True, 'AUTOTHROTTLE_START_DELAY': 2,
    'AUTOTHROTTLE_MAX_DELAY': 60, 'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
    'AUTOTHROTTLE_DEBUG': True}
def start_requests(self):...
yield scrapy.Request(self.login_url, self.parse_login)
def parse_login(self, response):...
print('Login')
print(response.url)
yield scrapy.FormRequest.from_response(response, formdata=self.login_data,
    callback=self.start_crawl)
def start_crawl(self, response):...
print('Start Crawl')
print(response.url)
key_extractor = KeyExtractor()
while key_extractor.hasMoreProfileLinks():
links = key_extractor.getMoreProfileLinks()
def parse(self, response):...
for link in links:
url_parts = response.url.split('/')
about_link = link
if len(url_parts) == 5:
couch_link = link + '/couch'
print('Mainpage')
print('Not Mainpage')
photos_link = link + '/photos'
page_name = 'Main'
page_name = url_parts[len(url_parts) - 1]
references_link = link + '/references'
profile_name = url_parts[len(url_parts) - 1]
profile_name = url_parts[len(url_parts) - 2]
friends_link = link + '/friends'
websites = {'_id': profile_name, 'URL': response.url, page_name: response.
    body.decode('utf-8')}
favorites_link = link + '/favorites'
yield {'websites': websites}
link_list = [about_link, couch_link, photos_link, references_link,
    friends_link, favorites_link]
for sub_link in link_list:
yield scrapy.Request(url=sub_link, callback=self.parse)
