class PathTraversal(Attack):
    def run(self, handler):
        params = handler.params

        try:
            path = params.get('path', ['docs/cursus.txt'])[0]
            if '://' not in path:
                file = open(os.path.abspath(path), 'rb')
            else:
                file = urllib.request.urlopen(path)

            file = html.escape(file.read().decode())
        except:
            file = 'File not found...'

        content = '<pre><code>{}</code></pre>'.format(file)

        return content
