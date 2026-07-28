def specific_info(self):...
return """Username: %s
Password: %s
""" % (self.username, self.password
    ) + GenericRequest.specific_info(self)
