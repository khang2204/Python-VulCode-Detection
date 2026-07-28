def post_ad_using_data(self, data, image_files=[]):...
"""docstring"""
resp = self.session.get(
    'https://www.kijiji.ca/p-admarkt-post-ad.html?categoryId=773')
token_regex = "initialXsrfToken: '\\S+'"
image_upload_token = re.findall(token_regex, resp.text)[0].strip(
    "initialXsrfToken: '").strip("'")
imageList = self.upload_image(image_upload_token, image_files)
data['images'] = ','.join(imageList)
data['ca.kijiji.xsrf.token'] = get_token(resp.text, 'ca.kijiji.xsrf.token')
data['postAdForm.fraudToken'] = get_token(resp.text, 'postAdForm.fraudToken')
data['postAdForm.description'] = data['postAdForm.description'].replace('\\n',
    '\n')
new_ad_url = 'https://www.kijiji.ca/p-submit-ad.html'
resp = self.session.post(new_ad_url, data=data)
if not len(data.get('postAdForm.title', '')) >= 10:
if int(resp.status_code) != 200 or 'Delete Ad?' not in resp.text:
if 'There was an issue posting your ad, please contact Customer Service.' in resp.text:
new_cookie_with_ad_id = resp.headers['Set-Cookie']
ad_id = re.search('\\d+', new_cookie_with_ad_id).group()
return ad_id
