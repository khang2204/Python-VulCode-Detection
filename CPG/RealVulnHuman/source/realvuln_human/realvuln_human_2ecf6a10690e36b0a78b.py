output_file.write(file1['body'])
        output_file.close()
        self.finish("file" + final_filename + " is uploaded")


class ContentHandler(tornado.web.RequestHandler):

    def get(self):
        file_name = self.get_argument("file", default="car")
        content = ''
        read_file = io.open("read/" + file_name, 'rb')
        content = read_file.read()
        read_file.close()
        self.write(content)


class SearchHandler(tornado.web.RequestHandler):

    def get(self):
        print "GET ", self.request.uri
        query = self.get_argument("q", default="Query")
