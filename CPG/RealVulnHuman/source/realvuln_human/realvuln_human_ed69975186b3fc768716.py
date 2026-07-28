setTimeout(function() {{
                    window.location.replace('{path}');
                }}, 3000);
            </script>
        '''.format(path=path)

        return content


class ExecutionAfterRedirect(Attack):
    def run(self, handler):
        cookie = handler.cookie

        content = '''
            <ul>
                <li><a href=#>Manage Users</a></li>
                <li><a href=#>Update Database Settings</a></li>
            </ul>
        '''

        if not cookie:
            content += "<script>window.location = '/login';</script>"

        return content


class CommandInjection(Attack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        domain = 'www.google.com'
        payload = ';ifconfig' if os.name != 'nt' else '&ipconfig'
        payload = urlparse.quote_plus(payload)
        self.evil_path = '{}?domain={}{}'.format(self.route, domain, payload)
