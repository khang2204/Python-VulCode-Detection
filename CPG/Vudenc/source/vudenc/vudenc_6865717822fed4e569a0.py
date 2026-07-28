def _get_captcha(self, headers):...
"""docstring"""
lang = headers.get('lang', 'en')
if lang == 'cn':
api = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=cn'
api = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
resp = self.session.get(api, headers=headers)
show_captcha = re.search('true', resp.text)
if show_captcha:
put_resp = self.session.put(api, headers=headers)
return ''
img_base64 = re.findall('"img_base64":"(.+)"', put_resp.text, re.S)[0].replace(
    '\\n', '')
f.write(base64.b64decode(img_base64))
img = Image.open('./captcha.jpg')
if lang == 'cn':
plt.imshow(img)
img.show()
print('点击所有倒立的汉字，按回车提交')
capt = input('请输入图片里的验证码：')
points = plt.ginput(7)
self.session.post(api, data={'input_text': capt}, headers=headers)
capt = json.dumps({'img_size': [200, 44], 'input_points': [[i[0] / 2, i[1] /
    2] for i in points]})
return capt
