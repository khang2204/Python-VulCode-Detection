def test_should_delete_a_playlist_and_remove_all_its_videos():...
populate_test_database()
create_playlist('first playlist')
create_video(1, 'the title of the video', 'the url of the video', 1)
create_video(1, 'the title of the video', 'the url of the video', 2)
response = test_app.delete('/playlists/1')
assert response.json['status'] == 'OK'
response2 = test_app.get('/playlists/1')
assert response2.json['status'] == 'OK'
assert response2.json['data'] == None
response3 = test_app.get('/videos/1')
assert response3.json['status'] == 'OK'
assert response3.json['data'] == []
