import pytest
import bottle
import webtest
import MySQLdb
import os
from logging import getLogger
from bottle_mysql import Plugin
from video import video_api
from playlist import playlist_api
from database import populate_test_database
logger = getLogger()
app = bottle.default_app()
plugin = Plugin(dbuser=os.environ['USER'], dbpass=os.environ['PASSWORD'],
    dbname='test')
app.install(plugin)
test_app = webtest.TestApp(app)
def create_video(playlist_id, title, thumbnail, position):...
db = connect_to_database()
cursor = db.cursor()
cursor.execute(
    "INSERT INTO video (playlist_id, title, thumbnail, position) VALUES('{playlist_id}', '{title}', '{thumbnail}', '{position}');"
    .format(playlist_id=playlist_id, title=title, thumbnail=thumbnail,
    position=position))
db.commit()
db.close()
def create_playlist(name):...
db = connect_to_database()
cursor = db.cursor()
cursor.execute(
    "INSERT INTO playlist (name, video_position) VALUES('{name}', 0);".
    format(name=name))
db.commit()
db.close()
def connect_to_database():...
db = MySQLdb.connect('localhost', 'root', os.environ['PASSWORD'], 'test')
return db
