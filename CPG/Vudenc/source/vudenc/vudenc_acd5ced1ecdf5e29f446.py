def delete_ad(args):...
"""docstring"""
api = kijiji_api.KijijiApi()
api.login(args.username, args.password)
api.delete_ad(args.id)
