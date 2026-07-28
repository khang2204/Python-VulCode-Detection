from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import requests
import time
def __init__(self, wiki):...
self.MAX_P_CHECKS = 5
self.MAX_CRAWLS = 1
self.MAX_PATH_LENGTH = 50
self.TARGET = 'Philosophy'
self.DOMAIN = 'https://en.wikipedia.org'
self.start_wiki = 'Special:Random' if not wiki else wiki
self.path_lengths = []
self.wiki_to_target_length = {}
self.completed_path = 0
self.invalid_path = 0
def build_url(self, wiki_topic, add_wiki_text):...
if add_wiki_text:
url = self.DOMAIN + '/wiki/' + wiki_topic
url = self.DOMAIN + wiki_topic
return url
