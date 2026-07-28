from __future__ import absolute_import, division
from abc import abstractmethod
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, pyqtSignal
from TriblerGUI.defs import ACTION_BUTTONS
from TriblerGUI.utilities import format_size, pretty_date
"""
    The base model for the tables in the Tribler GUI.
    It is specifically designed to fetch data from a remote data source, i.e. over a RESTful API.
    """
on_sort = pyqtSignal(str, bool)
def __init__(self, parent=None):...
super(RemoteTableModel, self).__init__(parent)
self.data_items = []
self.item_load_batch = 50
self.total_items = 0
self.infohashes = {}
@abstractmethod...
@abstractmethod...
def reset(self):...
self.beginResetModel()
self.data_items = []
self.endResetModel()
def sort(self, column, order):...
self.reset()
self.on_sort.emit(self.columns[column], bool(order))
def add_items(self, new_data_items):...
if not new_data_items:
return
old_end = self.rowCount()
new_end = self.rowCount() + len(new_data_items)
self.beginInsertRows(QModelIndex(), old_end, new_end - 1)
self.data_items.extend(new_data_items)
self.endInsertRows()
column_headers = []
column_width = {}
column_flags = {}
column_display_filters = {}
def __init__(self, hide_xxx=False):...
RemoteTableModel.__init__(self, parent=None)
self.data_items = []
self.column_position = {name: i for i, name in enumerate(self.columns)}
self.edit_enabled = False
self.hide_xxx = hide_xxx
def headerData(self, num, orientation, role=None):...
if orientation == Qt.Horizontal and role == Qt.DisplayRole:
return self.column_headers[num]
def _get_remote_data(self, start, end, **kwargs):...
def _set_remote_data(self):...
def rowCount(self, parent=QModelIndex()):...
return len(self.data_items)
