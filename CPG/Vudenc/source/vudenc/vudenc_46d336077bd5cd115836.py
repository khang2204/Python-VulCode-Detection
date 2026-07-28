def upload_image(self, token, image_files=[]):...
"""docstring"""
image_urls = []
image_upload_url = 'https://www.kijiji.ca/p-upload-image.html'
for img_file in image_files:
for i in range(0, 3):
return [image for image in image_urls if image is not None]
files = {'file': img_file}
r = self.session.post(image_upload_url, files=files, headers={
    'x-ebay-box-token': token})
if r.status_code != 200:
print(r.status_code)
image_tree = json.loads(r.text)
print('Image Upload failed on try #{}'.format(i + 1))
img_url = image_tree['thumbnailUrl']
print('Image Upload success on try #{}'.format(i + 1))
image_urls.append(img_url)
