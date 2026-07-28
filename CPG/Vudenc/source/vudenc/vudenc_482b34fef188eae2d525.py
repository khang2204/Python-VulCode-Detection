def run(self):...
ti = time.time()
print('=' * 25)
print("""
[*]Target: {}
[*]Date: {}""".format(target.get(), datetime.now().
    strftime('%d/%m/%Y %H:%M:%S')))
crl = [target.get()]
if crawl.get() == 'On':
crl += bane.crawl(target.get(), bypass=True)
pr = proxy.get()
if len(pr) == 0:
pr = None
if method.get() == 'GET':
get = True
if method.get() == 'POST':
post = False
get = False
get = True
fresh = False
post = True
post = True
if refresh.get() == 'On':
fresh = True
ck = None
c = cookie.get()
if len(c) > 0:
ck = c
for x in crl:
if stop == True:
print("""[*]Test was finished at: {}
[*]Duration: {} seconds
""".format(
    datetime.now().strftime('%d/%m/%Y %H:%M:%S'), int(time.time() - ti)))
print('[*]URL: {}'.format(x))
print('=' * 25)
bane.xss(x, payload=payload.get(), proxy=pr, get=get, post=post, user_agent
    =user_agent.get(), fresh=fresh, cookie=ck)
