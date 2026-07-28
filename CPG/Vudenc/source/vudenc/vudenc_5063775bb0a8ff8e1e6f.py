def zmi_body_content(self, *args, **kwargs):...
request = self.REQUEST
response = request.RESPONSE
return self.getBodyContent(request)
