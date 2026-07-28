def test_should_update_a_video_position():...
populate_test_database()
create_playlist('first playlist')
create_video(1, 'title', 'thumbnail', 1)
create_video(1, 'title2', 'thumbnail2', 2)
create_video(1, 'title3', 'thumbnail3', 3)
create_video(1, 'title4', 'thumbnail4', 4)
response = test_app.put('/videos/4/1/2')
assert response.json['status'] == 'OK'
response2 = test_app.get('/videos/1')
assert response2.json['status'] == 'OK'
assert response2.json['data'] == [dict(id=1, title='title', thumbnail=
    'thumbnail', position=1), dict(id=4, title='title4', thumbnail=
    'thumbnail4', position=2), dict(id=2, title='title2', thumbnail=
    'thumbnail2', position=3), dict(id=3, title='title3', thumbnail=
    'thumbnail3', position=4)]
