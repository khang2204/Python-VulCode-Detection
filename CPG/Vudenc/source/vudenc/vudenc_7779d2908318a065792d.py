def qa_button_text(self):...
if self.get_qa_status():
return 'QA Complete'
if self.qa_begun:
return 'Continue QA'
return 'Begin QA'
