def specific_info(self):...
return """Task: %s (ID %d)
File: %s
""" % (self.task[1], self.task[0], self
    .source_path) + GenericRequest.specific_info(self)
