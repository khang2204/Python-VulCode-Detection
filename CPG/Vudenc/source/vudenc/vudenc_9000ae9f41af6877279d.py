@api.route('/songs/<int:id>')...
song = Song.query.filter_by(id=id).first()
if not song:
return route_not_found(song)
return make_response(jsonify(song.to_json()), 200)
