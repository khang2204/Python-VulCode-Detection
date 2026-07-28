def nuke(args):...
"""docstring"""
api = kijiji_api.KijijiApi()
api.login(args.username, args.password)
allAds = api.get_all_ads()
[api.delete_ad(adId) for adName, adId in allAds]
