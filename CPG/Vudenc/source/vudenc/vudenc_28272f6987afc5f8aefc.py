def test_should_return_all_the_videos():...
populate_test_database()
create_playlist('first playlist')
create_playlist('second playlist')
create_video(1, 'f title', 'f url', 1)
create_video(1, 's title', 's url', 2)
create_video(1, 't title', 't url', 3)
create_video(2, 'f title', 'f url', 1)
create_video(2, 'fh title', 'fh url', 2)
response = test_app.get('/videos')
assert response.json['status'] == 'OK'
assert response.json['data'] == [dict(id=1, playlist_id=1, title='f title',
    thumbnail='f url', position=1), dict(id=2, playlist_id=1, title=
    's title', thumbnail='s url', position=2), dict(id=3, playlist_id=1,
    title='t title', thumbnail='t url', position=3), dict(id=4, playlist_id
    =2, title='f title', thumbnail='f url', position=1), dict(id=5,
    playlist_id=2, title='fh title', thumbnail='fh url', position=2)]
