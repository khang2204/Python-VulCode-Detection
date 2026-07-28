def create_frame(self, F):...
new_frame = SearchPage(self.container, self)
self.frames[SearchPage] = new_frame
new_frame.grid(row=0, column=0, sticky='nsew')
self.show_frame(new_frame)
