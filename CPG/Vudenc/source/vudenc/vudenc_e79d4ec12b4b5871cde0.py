def __init__(self, parent, controller):...
tk.Frame.__init__(self, parent)
label = tk.Label(self, text='Login Page', font=controller.titleFont)
label.pack(pady=10, padx=10)
enterAppButton = tk.Button(self, text='Start Using Raspi-Telxon!', font=
    controller.itemFont, command=lambda : controller.show_frame(SearchPage))
enterAppButton.pack(pady=5)
exitAppButton = tk.Button(self, text='Quit', font=controller.itemFont,
    command=lambda : sys.exit(0))
exitAppButton.pack(pady=5)
