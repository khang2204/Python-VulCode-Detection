def delete_ad_using_title(self, title):...
"""docstring"""
allAds = self.get_all_ads()
[self.delete_ad(i) for t, i in allAds if t.strip() == title.strip()]
