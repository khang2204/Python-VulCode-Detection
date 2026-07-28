def setCredentials(self):...
self.win = Toplevel()
self.win.title = 'Input JIRA Login'
self.username_static_text = Label(self.win, text='Username:')
self.username_static_text.grid(column=0, row=0, sticky='E')
self.username_field = Entry(self.win)
self.username_field.configure(background=self.colorGreyBackground,
    foreground=self.colorWhiteText)
self.username_field.grid(column=1, row=0, sticky='W')
self.password_static_text = Label(self.win, text='Password:')
self.password_static_text.grid(column=0, row=1, sticky='E')
self.password_field = Entry(self.win, show='*')
self.password_field.configure(background=self.colorGreyBackground,
    foreground=self.colorWhiteText)
self.password_field.grid(column=1, row=1, sticky='W')
self.submit_button = Button(self.win, text='Save Credentials', command=self
    .setLoginInfo)
self.submit_button.grid(column=1, row=2, columnspan=2)
