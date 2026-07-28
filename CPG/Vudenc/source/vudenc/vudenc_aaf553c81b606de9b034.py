def create_video(playlist_id, title, thumbnail, position, db):...
db.execute(
    "INSERT INTO video (playlist_id, title, thumbnail, position) VALUES({playlist_id}, '{title}', '{thumbnail}', {position});"
    .format(playlist_id=playlist_id, title=title, thumbnail=thumbnail,
    position=position))
