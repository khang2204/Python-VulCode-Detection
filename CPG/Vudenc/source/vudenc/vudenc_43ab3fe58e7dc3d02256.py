def __init__(self, parent, controller):...
tk.Frame.__init__(self, parent)
self.controller = controller
ID, UPC, name, imageURI = controller.get_result()
load = Image.open(imageURI)
render = ImageTk.PhotoImage(load)
img_label = tk.Label(self, image=render)
img_label.image = render
img_label.pack(side='right')
name_label = tk.Label(self, text='Product: ' + name, font=controller.titleFont)
name_label.pack(pady=10, padx=10, anchor='nw')
upc_label = tk.Label(self, text='UPC: ' + UPC, font=controller.itemFont)
upc_label.pack(pady=10, padx=10, anchor='nw')
new_search_button = tk.Button(self, text='New Search', font=controller.
    itemFont, command=lambda : self.new_search())
new_search_button.pack(side='left', pady=10, padx=10, anchor='sw')
exit_app_button = tk.Button(self, text='Quit', font=controller.itemFont,
    command=lambda : sys.exit(0))
exit_app_button.pack(side='left', pady=10, padx=10, anchor='sw')
