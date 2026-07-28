"""
Utilises the free wordnik API.

Requires an API key.

Sign up:
    http://www.wordnik.com/signup

Get a key:
    http://developer.wordnik.com/

They seem to say they will send an email, however, I never got one. I checked
in my settings and found the API key there.

The key should be stored in the tokens.json file under "wordnik\"
"""
import typing
import wordnik.swagger as swagger
import wordnik.WordApi as wordapi
import wordnik.models.Definition as definition
import neko
_api_endpoint = 'http://api.wordnik.com/v4'
_dictionaries = 'all'
def __init__(self):...
self.__token = neko.get_token('wordnik')
self.logger.info(f'Opening API client for Wordnik to {_api_endpoint}')
self.client = swagger.ApiClient(self.__token, _api_endpoint)
@neko.command(name='def', aliases=['define', 'def', 'dfn'], brief=...
"""docstring"""
def _define():...
api = wordapi.WordApi(self.client)
return api.getDefinitions(word, sourceDictionaries=_dictionaries,
    includeRelated=True)
