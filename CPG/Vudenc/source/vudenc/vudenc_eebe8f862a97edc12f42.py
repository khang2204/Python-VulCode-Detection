def post_ad(args):...
"""docstring"""
[data, imageFiles] = get_inf_details(args.inf_file)
attempts = 1
while not check_ad(args) and attempts < 5:
if attempts > 1:
if not check_ad(args):
print('Failed Attempt #' + str(attempts) + ', trying again.')
attempts += 1
print('Failed Attempt #' + str(attempts) + ', giving up.')
api = kijiji_api.KijijiApi()
api.login(args.username, args.password)
api.post_ad_using_data(data, imageFiles)
sleep(180)
