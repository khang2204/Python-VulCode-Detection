def _define():...
api = wordapi.WordApi(self.client)
return api.getDefinitions(word, sourceDictionaries=_dictionaries,
    includeRelated=True)
