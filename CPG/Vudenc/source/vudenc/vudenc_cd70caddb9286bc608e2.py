def __init__(self, parent, controller):...
tk.Frame.__init__(self, parent)
self.controller = controller
statusbar = tk.Frame(self)
statusbar.pack(side='top', fill='x')
self.statusbar = statusbar
navbar = tk.Frame(self)
navbar.pack(side='bottom', fill='x')
self.navbar = navbar
UPC_Label = tk.Label(self, text='UPC', font=controller.titleFont)
UPC_Label.pack(pady=10, padx=10, anchor='center')
self.UPC_Entry = tk.Entry(self)
self.UPC_Entry.pack(pady=10, padx=10, anchor='center')
backButton = tk.Button(navbar, text='Back', font=controller.itemFont,
    command=lambda : controller.show_frame(StartPage))
backButton.pack(side='left', pady=10, padx=10)
Search_Button = tk.Button(navbar, text='Search', font=controller.itemFont,
    command=self.search)
Search_Button.pack(side='left', pady=10, padx=10)
exitAppButton = tk.Button(navbar, text='Quit', font=controller.itemFont,
    command=lambda : sys.exit(0))
exitAppButton.pack(side='left', pady=10, padx=10)
