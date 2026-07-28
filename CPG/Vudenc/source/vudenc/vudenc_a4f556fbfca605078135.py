def __init__(self):...
self.login_url = LOGIN_URL
self.login_api = LOGIN_API
self.login_data = FORM_DATA.copy()
self.session = requests.session()
self.session.headers = HEADERS.copy()
self.session.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')
