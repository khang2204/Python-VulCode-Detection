def repost_ad(args):...
"""docstring"""
api = kijiji_api.KijijiApi()
api.login(args.username, args.password)
delAdName = ''
for line in open(args.inf_file, 'rt'):
[key, val] = line.strip().rstrip('\n').split('=')
api.delete_ad_using_title(delAdName)
print('Did not find an existing ad with matching title, skipping ad deletion')
sleep(180)
if key == 'postAdForm.title':
print('Existing ad deleted before reposting')
post_ad(args)
delAdName = val
