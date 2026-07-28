return content


class XSSReflected(Attack):
    def run(self, handler):
        params = handler.params

        content = params.get('msg', '')
        if len(content):
            content = content[0]
        else:
            content = 'No messages...'

        return content


class XSSStored(Attack):
    def run(self, handler):
        params = handler.params
        connection = handler.server.connection
