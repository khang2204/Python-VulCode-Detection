def specific_info(self):...
return """Task: %s (ID %d)
File: %s
""" % (self.task[1], self.task[0], repr
    (self.filenames)) + GenericRequest.specific_info(self)
