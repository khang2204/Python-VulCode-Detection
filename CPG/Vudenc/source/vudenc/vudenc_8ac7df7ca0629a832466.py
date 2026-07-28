def test_should_create_a_video():...
populate_test_database()
create_playlist('first playlist')
response = test_app.post('/videos/1/title/thumbnail')
assert response.json['status'] == 'OK'
response2 = test_app.post('/videos/1/title2/thumbnail2')
assert response2.json['status'] == 'OK'
response3 = test_app.get('/videos/1')
assert response3.json['status'] == 'OK'
assert response3.json['data'] == [dict(id=1, title='title', thumbnail=
    'thumbnail', position=1), dict(id=2, title='title2', thumbnail=
    'thumbnail2', position=2)]
