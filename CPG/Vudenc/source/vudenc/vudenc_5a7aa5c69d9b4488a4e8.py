def is_logged_in(self):...
"""docstring"""
index_page_text = self.session.get('https://www.kijiji.ca/m-my-ads.html/').text
return 'Sign Out' in index_page_text
