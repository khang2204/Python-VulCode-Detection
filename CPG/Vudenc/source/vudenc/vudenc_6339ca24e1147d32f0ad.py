def errorNotification(self, error_message):...
self.error_window = Toplevel()
self.error_window.title = 'ERROR - PLEASE READ'
error_message_text = Message(self.error_window, text=error_message, width=500)
error_message_text.grid(row=0, column=0, columnspan=3)
close_button_error = Button(self.error_window, text='Ok', command=lambda :
    self.error_window.destroy())
close_button_error.grid(row=1, column=1)
