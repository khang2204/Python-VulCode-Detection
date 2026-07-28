def post(self):...
self.check_xsrf()
if self.check() == False:
return self.redirect('/')
fileitem = self.request.files['filename']
if fileitem.filename:
filetype = imghdr.what(fileitem.file)
return self.redirect('/user')
filesize = self.get_filesize(fileitem.file)
if filesize > MAX_FILE_SIZE:
return self.redirect('/ftypeerror')
if filetype is 'jpeg' or filetype is 'png' or filetype is 'gif':
m = hashlib.md5()
return self.redirect('/ftypeerror')
m.update(self.email)
email_md5 = m.hexdigest()
path = 'images/' + email_md5
path = os.path.join(os.path.dirname(__file__), '..', path)
open(path, 'wb').write(fileitem.file.read())
return self.redirect('/user')
