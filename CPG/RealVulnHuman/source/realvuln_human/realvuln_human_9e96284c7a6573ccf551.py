def on_get(self, req, resp):
        raise falcon.HTTPFound("/vulnpy")


class FileUpload(object):
    def on_post(self, req, resp):
        user_input = req._params["upload"].file.read()

        digest = hexlify(md5(user_input).digest()).decode("utf8")

        cmd = "echo " + str(user_input[:10])
        os.system(cmd)

        resp.status = falcon.HTTP_200
        resp.media = {"status": "ok", "md5": digest}


def thread_function(user_input):
    """This is intented to test Contrast specific functionality!"""

    print("starting background thread")
