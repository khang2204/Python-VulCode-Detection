</table>'''.format(rows)

        return content


class UnvalidatedRedirect(Attack):
    def run(self, handler):
        params = handler.params

        path = params.get('path', '/')[0]
        content = '''
            <script>
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
