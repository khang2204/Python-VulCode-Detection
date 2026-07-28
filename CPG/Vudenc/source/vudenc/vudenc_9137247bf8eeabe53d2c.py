def get_all_ads(self):...
"""docstring"""
resp = self.session.get('https://www.kijiji.ca/m-my-ads.html')
user_id = get_token(resp.text, 'userId')
my_ads_url = (
    'https://www.kijiji.ca/j-get-my-ads.json?_=1&currentOffset=0&isPromoting=false&show=ACTIVE&user={}'
    .format(user_id))
my_ads_page = self.session.get(my_ads_url)
my_ads_tree = json.loads(my_ads_page.text)
ad_ids = [entry['id'] for entry in my_ads_tree['myAdEntries']]
ad_names = [entry['title'] for entry in my_ads_tree['myAdEntries']]
return zip(ad_names, ad_ids)
