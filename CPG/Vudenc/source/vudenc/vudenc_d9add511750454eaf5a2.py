def __init__(self):...
self.__token = neko.get_token('wordnik')
self.logger.info(f'Opening API client for Wordnik to {_api_endpoint}')
self.client = swagger.ApiClient(self.__token, _api_endpoint)
