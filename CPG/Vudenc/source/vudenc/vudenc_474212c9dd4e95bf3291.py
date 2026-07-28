def upload_avatar(self, ud):...
if 'avatar_uploaded' in ud[0] and ud[0]['avatar_uploaded'] is True:
return
files = []
for sd in os.walk(c.av_dir):
files.extend(sd[2])
av = os.path.join(sd[0], random.choice(files))
self.log.info('Uploading %s as new avatar', av)
self.site.uploadavatar('0', av)
ud[0]['avatar'] = av
ud[0]['avatar_uploaded'] = True
