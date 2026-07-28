def test_should_reorder_video_position_given_a_deleted_video():...
populate_test_database()
create_playlist('first playlist')
response = test_app.post('/videos/1/title/thumbnail')
assert response.json['status'] == 'OK'
response2 = test_app.post('/videos/1/title2/thumbnail2')
assert response2.json['status'] == 'OK'
response3 = test_app.post('/videos/1/title3/thumbnail3')
assert response3.json['status'] == 'OK'
response4 = test_app.delete('/videos/2/1')
assert response4.json['status'] == 'OK'
response5 = test_app.get('/videos/1')
assert response.json['status'] == 'OK'
assert response5.json['data'] == [dict(id=1, title='title', thumbnail=
    'thumbnail', position=1), dict(id=3, title='title3', thumbnail=
    'thumbnail3', position=2)]
response6 = test_app.get('/playlists/1')
assert response6.json['status'] == 'OK'
assert response6.json['data'] == dict(id=1, name='first playlist',
    video_position=2)
