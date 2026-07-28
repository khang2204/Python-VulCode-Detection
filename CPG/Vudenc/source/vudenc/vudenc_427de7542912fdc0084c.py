def retrieve_videos(db):...
db.execute(
    'SELECT id, playlist_id, title, thumbnail, position from video ORDER BY playlist_id ASC, position ASC;'
    )
rows = db.fetchall()
return rows
