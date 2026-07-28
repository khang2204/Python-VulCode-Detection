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
