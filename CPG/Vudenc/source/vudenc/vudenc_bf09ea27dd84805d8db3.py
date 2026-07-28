def show_ads(args):...
"""docstring"""
api = kijiji_api.KijijiApi()
api.login(args.username, args.password)
[print("{} '{}'".format(adId, adName)) for adName, adId in api.get_all_ads()]
