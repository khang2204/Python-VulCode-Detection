def test_should_delete_a_video_given_an_id_and_update_playlist_video_position(...
populate_test_database()
create_playlist('first playlist')
response = test_app.post('/videos/1/title/thumbnail')
assert response.json['status'] == 'OK'
response2 = test_app.delete('/videos/1/1')
assert response2.json['status'] == 'OK'
response3 = test_app.get('/videos/1')
assert response3.json['status'] == 'OK'
assert response3.json['data'] == []
response4 = test_app.get('/playlists/1')
assert response4.json['status'] == 'OK'
assert response4.json['data'] == dict(id=1, name='first playlist',
    video_position=0)
