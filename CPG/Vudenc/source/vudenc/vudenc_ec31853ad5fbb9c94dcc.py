def start_crawl(self, response):...
print('Start Crawl')
print(response.url)
key_extractor = KeyExtractor()
while key_extractor.hasMoreProfileLinks():
links = key_extractor.getMoreProfileLinks()
for link in links:
about_link = link
couch_link = link + '/couch'
photos_link = link + '/photos'
references_link = link + '/references'
friends_link = link + '/friends'
favorites_link = link + '/favorites'
link_list = [about_link, couch_link, photos_link, references_link,
    friends_link, favorites_link]
for sub_link in link_list:
yield scrapy.Request(url=sub_link, callback=self.parse)
