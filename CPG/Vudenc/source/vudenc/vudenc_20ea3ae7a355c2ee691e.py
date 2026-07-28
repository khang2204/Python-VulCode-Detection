def get_cws_browser(user_id):...
if cws_browser is None:
cws_browser = Browser()
return cws_browser
username = created_users[user_id]['username']
password = created_users[user_id]['password']
lr = CWSLoginRequest(cws_browser, username, password, base_url=CWS_BASE_URL)
cws_browser.login(lr)
