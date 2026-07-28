def get_user_test_info(self):...
soup = BeautifulSoup(self.res_data, 'html.parser')
info = {}
tag = soup.findAll(id='user_test_status')[0]
info['status'] = tag.text.strip()
tags = soup.findAll(id='compilation')
if tags:
content = tags[0]
info['compile_output'] = None
info['compile_output'] = content.pre.text.strip()
return info
