def testEncodeMultipartFormData(self):...
fields = [('x', 'y'), (1, 2)]
files = [('key', 'filename', 'file data')]
content_type, body = url_helper.EncodeMultipartFormData()
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertEqual('', body)
content_type, body = url_helper.EncodeMultipartFormData(fields=fields)
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertTrue('name="x"\r\n\r\ny' in body, body)
self.assertTrue('name="1"\r\n\r\n2' in body, body)
content_type, body = url_helper.EncodeMultipartFormData(files=files)
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertTrue('name="key"; filename="filename"' in body, body)
self.assertTrue('file data' in body, body)
content_type, body = url_helper.EncodeMultipartFormData(fields=fields,
    files=files)
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertTrue('name="x"\r\n\r\ny' in body, body)
self.assertTrue('name="1"\r\n\r\n2' in body, body)
