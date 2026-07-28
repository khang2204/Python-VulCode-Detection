""" Contains simple tools for querying the lastfm_tags.db file


Notes
-----
The lastfm database contains 3 tables: tids, tags, tid_tag.
- tids, 1-column table containing the track ids.
- tid_tags, contains 3 columns:
    - tid: rowid of the track id in the tids table.
    - tag: rowid of the tag that belongs to the tid in the same row.
    - val: number between 0 and 100 (guessing this is how accurate the tag is?)
- tags, 1-column table containing the tags.

IMPORTANT: If using this script elsewhere than on Boden then run set_path(new_path) to
set the path of the database. Otherwise it will use the default path, which is the path
to the database on Boden.

Functions
---------
- set_path
    Set path to the lastfm_tags.db.
"""
import sqlite3
path = '/srv/data/msd/lastfm/SQLITE/lastfm_tags.db'
def set_path(new_path):...
"""docstring"""
path = new_path
""" Opens a SQLite connection to the last.fm database. Provides methods to perform advanced queries on it.

    Methods
    -------
    - tid_to_tid_nums
        Get tid_num given tid.

    - tid_num_to_tid
        Get tid given tid_num.

    - tid_num_to_tag_nums
        Get tag_num given tid_num.

    - tag_num_to_tag
        Get tag given tag_num.

    - tag_to_tag_num
        Get tag_num given tag.

    - get_tags
        Get a list of tags associated to given tid.

    - get_tags_dict
        Get a dict with tids as keys and a list of its tags as value.

    - tid_tag_count
        Get a dict with tids as keys and its number of tags as value.

    - filter_tags
        Filter list of tids based on minimum number of tags.

    - tag_count
        Get a dict with the tags associated to tids as keys and their count number as values.
    """
def __init__(self, path):...
self.conn = sqlite3.connect(path)
self.c = self.conn.cursor()
def __del__(self):...
self.conn.close()
def query(self, query):...
return self.c.execute(query)
