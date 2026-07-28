def __init__(self):...
tk.Tk.__init__(self)
self.title('Raspi-Telxon')
self.titleFont = font.Font(family='Helvetica', size=24)
self.itemFont = font.Font(family='Helvetica', size=18)
container = tk.Frame(self)
container.pack(side='top', fill='both', expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
self.frames = {}
self.result = ''
self.container = container
for F in (StartPage, SearchPage):
frame = F(container, self)
self.show_frame(StartPage)
self.frames[F] = frame
frame.grid(row=0, column=0, sticky='nsew')
