def run(self, handler):
        params = handler.params

        content = 'Try <a href="{}">this</a> or <a href="{}">this</a>...'.format(self.good_path, self.evil_path)

        if handler.risk < 3:
            content = self.warning.format(handler.risk)
        elif 'object' in params:
            object = params.get('object', '')[0]
            content = str(pickle.loads(base64.urlsafe_b64decode(object)))

        return content


class PathTraversal(Attack):
    def run(self, handler):
        params = handler.params

        try:
            path = params.get('path', ['docs/cursus.txt'])[0]
