def check_ad(args):...
"""docstring"""
api = kijiji_api.KijijiApi()
api.login(args.username, args.password)
AdName = ''
for line in open(args.inf_file, 'rt'):
[key, val] = line.strip().rstrip('\n').split('=')
allAds = api.get_all_ads()
if key == 'postAdForm.title':
return [t for t, i in allAds if t == AdName]
AdName = val
