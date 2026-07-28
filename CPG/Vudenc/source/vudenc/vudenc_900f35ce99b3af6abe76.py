@api.route('/songs/', methods=['POST'])...
if request.headers['content_type'] == 'application/json':
payload = request.get_json()
message = 'that aint json'
if not request.json or not 'title' in payload or not 'artist' in payload or not 'url' in payload:
return bad_request(message)
message = 'the payload aint right'
if Song.query.filter_by(url=payload['url']).first():
return bad_request(message)
message = 'this song already exists'
song = Song(title=payload['title'], artist=payload['artist'], url=payload[
    'url'], user=g.current_user)
message = 'this song already exists'
return bad_request(message)
db.session.add(song)
return bad_request(message)
db.session.commit()
return make_response(jsonify(song.to_json()), 200)
