def __init__(self, master, selenium):...
self.master = master
master.title('Jira Automation')
self.firefox = selenium
self.colorWhiteText = '#FFF'
self.colorGreyBackground = '#708090'
empty_spacer_1 = Label(master, text=' ')
empty_spacer_1.grid(column=0, row=0)
self.login_button = Button(master, text='JIRA Login', command=self.
    setCredentials)
self.login_button.grid(sticky='E', column=3, row=0)
self.summary_static_text = Label(master, text='Input Sync Summary:')
self.summary_static_text.grid(columnspan=4, sticky='W', row=1)
self.summary_field = Entry(root, width=61)
self.summary_field.configure(background=self.colorGreyBackground,
    foreground=self.colorWhiteText)
self.summary_field.grid(columnspan=4, column=0, row=2, sticky='W')
empty_spacer_2 = Label(master, text=' ')
empty_spacer_2.grid(column=0, row=3)
self.clarify_static_text = Label(master, text='Input Case Number:')
self.clarify_static_text.grid(columnspan=4, sticky='W', row=4)
self.clarify_field = Entry(root, width=61)
self.clarify_field.configure(background=self.colorGreyBackground,
    foreground=self.colorWhiteText)
self.clarify_field.grid(column=0, row=5, columnspan=4, sticky='W')
empty_spacer_3 = Label(master, text=' ')
empty_spacer_3.grid(column=0, row=6)
self.detailed_static_text = Label(master, text='Input Detailed Information')
self.detailed_static_text.grid(columnspan=4, sticky='W', row=7)
self.detailed_field = Text(root, height=35, width=79)
self.detailed_field.configure(background=self.colorGreyBackground,
    foreground=self.colorWhiteText)
self.detailed_field.grid(columnspan=4, row=8, column=0, sticky='W')
self.run_split_button = Button(master, text='Create JIRA', command=self.
    createCase)
self.run_split_button.grid(row=10, column=1, sticky='W')
self.close_button = Button(master, text='Close', command=master.quit)
self.close_button.grid(row=10, column=2, sticky='E')
