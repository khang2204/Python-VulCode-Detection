import sys
import tkinter as tk
import Controller as dbc
from PIL import Image, ImageTk
from tkinter import font
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
def create_frame(self, F):...
frame.grid(row=0, column=0, sticky='nsew')
new_frame = SearchPage(self.container, self)
self.frames[SearchPage] = new_frame
new_frame.grid(row=0, column=0, sticky='nsew')
self.show_frame(new_frame)
def remove_frame(self, frame):...
print('remove_frame: ' + str(frame))
self.frames.pop(frame, None)
def show_frame(self, cont):...
frame = self.frames[cont]
frame.tkraise()
def custom_frame(self):...
result_frame = ResultsPage(self.container, self)
self.frames[ResultsPage] = result_frame
result_frame.grid(row=0, column=0, sticky='nsew')
self.show_frame(ResultsPage)
def set_result(self, result):...
self.result = result
def get_result(self):...
return self.result
