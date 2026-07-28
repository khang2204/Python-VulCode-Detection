class MainHandler(tornado.web.RequestHandler):

    def get(self):
        print "GET ", self.request.uri
        self.render("index.html")


class UploadHandler(tornado.web.RequestHandler):

    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(
            string.ascii_lowercase + string.digits) for x in range(6))
        final_filename = fname + extension
        output_file = io.open("/tmp/" + final_filename, 'wb')
        output_file.write(file1['body'])
        output_file.close()
        self.finish("file" + final_filename + " is uploaded")


class ContentHandler(tornado.web.RequestHandler):

    def get(self):
        file_name = self.get_argument("file", default="car")
        content = ''
        read_file = io.open("read/" + file_name, 'rb')
        content = read_file.read()
