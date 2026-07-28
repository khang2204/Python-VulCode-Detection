def custom_frame(self):...
result_frame = ResultsPage(self.container, self)
self.frames[ResultsPage] = result_frame
result_frame.grid(row=0, column=0, sticky='nsew')
self.show_frame(ResultsPage)
