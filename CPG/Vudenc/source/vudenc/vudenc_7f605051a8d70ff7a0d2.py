def build_url(self, wiki_topic, add_wiki_text):...
if add_wiki_text:
url = self.DOMAIN + '/wiki/' + wiki_topic
url = self.DOMAIN + wiki_topic
return url
