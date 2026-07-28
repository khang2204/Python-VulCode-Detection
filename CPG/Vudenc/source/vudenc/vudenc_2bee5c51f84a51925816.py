def search(self):...
upc = ''
upcEntry = self.UPC_Entry.get()
if upcEntry == '':
emptyInputLabel = tk.Label(self.statusbar, text='UPC Cannot Be Empty', fg='red'
    )
if self.UPC_Entry.get() != '':
emptyInputLabel.pack()
self.View_Result_Button = tk.Button(self.navbar, text='View Result', font=
    self.controller.itemFont, command=lambda : self.controller.custom_frame())
self.View_Result_Button.pack(side='left', pady=10, padx=10)
upc = self.UPC_Entry.get()
database = dbc.DB_Connector()
database.some_upc = upc
result = database.fetch_product()
self.controller.set_result(result)
if result is None:
result_not_found = tk.Label(self, text='No Result Found!', font=self.
    controller.itemFont)
if result is not None:
result_not_found.pack()
result_found_notification = tk.Label(self, text='Results Found!', font=self
    .controller.itemFont)
self.View_Result_Button.config(state='disabled')
result_found_notification.pack()
self.View_Result_Button.config(state='normal')
