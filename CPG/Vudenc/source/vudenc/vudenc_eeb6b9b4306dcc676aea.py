def specific_info(self):...
return """Task: %s (ID %d)
Submission: %s
""" % (self.task[1], self.task[0],
    self.submission_num) + GenericRequest.specific_info(self)
