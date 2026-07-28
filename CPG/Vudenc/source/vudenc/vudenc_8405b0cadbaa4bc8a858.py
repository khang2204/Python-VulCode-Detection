def delete_ad(self, ad_id):...
"""docstring"""
my_ads_page = self.session.get('https://www.kijiji.ca/m-my-ads.html')
params = {'Action': 'DELETE_ADS', 'Mode': 'ACTIVE', 'needsRedirect':
    'false', 'ads':
    '[{{"adId":"{}","reason":"PREFER_NOT_TO_SAY","otherReason":""}}]'.
    format(ad_id), 'ca.kijiji.xsrf.token': get_token(my_ads_page.text,
    'ca.kijiji.xsrf.token')}
resp = self.session.post('https://www.kijiji.ca/j-delete-ad.json', data=params)
if 'OK' not in resp.text:
