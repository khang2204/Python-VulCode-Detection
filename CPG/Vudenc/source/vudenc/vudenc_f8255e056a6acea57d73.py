from gi.repository import Gio, Gdk, Gtk
from keepassgtk.logging_manager import LoggingManager
from keepassgtk.database_manager import DatabaseManager
from keepassgtk.create_database import CreateDatabase
from keepassgtk.container_page import ContainerPage
from keepassgtk.unlock_database import UnlockDatabase
import keepassgtk.config_manager
import os
from os.path import exists
import ntpath
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
application = NotImplemented
database_manager = NotImplemented
container = NotImplemented
override_dialog = NotImplemented
quit_dialog = NotImplemented
filechooser_creation_dialog = NotImplemented
headerbar = NotImplemented
first_start_grid = NotImplemented
logging_manager = LoggingManager(True)
opened_databases = []
databases_to_save = []
def __init__(self, *args, **kwargs):...
super().__init__(*args, **kwargs)
keepassgtk.config_manager.configure()
self.assemble_window()
def assemble_window(self):...
self.set_default_size(800, 500)
self.create_headerbar()
self.first_start_screen()
self.connect('delete-event', self.on_application_quit)
self.custom_css()
def create_headerbar(self):...
builder = Gtk.Builder()
builder.add_from_resource('/run/terminal/KeepassGtk/main_window.ui')
self.headerbar = builder.get_object('headerbar')
file_open_button = builder.get_object('open_button')
file_open_button.connect('clicked', self.open_filechooser, None)
file_new_button = builder.get_object('new_button')
file_new_button.connect('clicked', self.create_filechooser, None)
self.set_titlebar(self.headerbar)
def set_headerbar(self):...
self.set_titlebar(self.headerbar)
def get_headerbar(self):...
return self.headerbar
