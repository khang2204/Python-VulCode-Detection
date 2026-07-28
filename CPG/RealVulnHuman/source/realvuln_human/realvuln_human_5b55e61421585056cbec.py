'.Z': 'application/octet-stream',
    '.bz2': 'application/x-bzip2',
    '.xz': 'application/x-xz',
}

def find(self, path):
    path = 'static/svg/bug-fill.svg' if path == '/favicon.ico' else path
    ext = os.path.splitext(path)[1]
    try:
        if ext in ('.jpg', '.jpeg', '.png', '.woff', '.woff2', '.ttf', '.ico'):
            self.content = open('./{}'.format(path), 'rb')
        else:
            self.content = open('./{}'.format(path), 'r')
        self.content_type = self.guess_type(path)
        self.status_code = HTTPStatus.OK
        return True
    except:
        self.content = 'File not found'
        self.status_code = HTTPStatus.NOT_FOUND
        return False

def guess_type(self, path):
    base, ext = posixpath.splitext(path)
