def createCase(self):...
if self.password == None or self.username == None or self.password == ' ' or self.username == ' ':
self.errorNotification('Please login to JIRA first')
self.firefox.loadPage('https://devops.partech.com/jira/login.jsp', 'JIRA')
self.firefox.login(self.username, self.password)
self.firefox.createNewTicket()
self.firefox.inputDataToCase(self.summary_field.get(), self.detailed_field.
    get('1.0', END))
