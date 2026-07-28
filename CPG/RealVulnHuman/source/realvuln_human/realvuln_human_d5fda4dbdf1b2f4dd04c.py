class SessionFixation(Attack):
    def run(self, handler):
        params = handler.params
        cookie = handler.cookie

        if params.keys() & {'session'}:
            session = params.get('session')[0]
            cookie['SESSIONID'] = session

        path = params.get('path', '/')[0]
        content = '''
            <script>
                setTimeout(function() {{
                    window.location = '{path}';
                }}, 3000);
            </script>
        '''.format(path=path)

        return content


class SessionHijacking(Attack):
    def run(self, handler):
        cursor = handler.server.connection.cursor()
        content = 'Please login, <strong>Anonymous</strong>!'

        if 'SESSIONID' in handler.cookie:
