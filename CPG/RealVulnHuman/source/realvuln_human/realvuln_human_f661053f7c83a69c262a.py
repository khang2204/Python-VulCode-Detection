return jsonify({'error': 'invalid schema', 'schema': key_schema}), 400

    key = libapi.keygen(data['username'], data['password'])

    if key:
        return jsonify({'key': key}), 200
    else:
        return jsonify({'error': 'invalid login'}), 403


@mod_api.route('/post/<username>', methods=['GET'])
def do_post_list(username):
    posts = libposts.get_posts(username)

    return jsonify(posts)


@mod_api.route('/post', methods=['POST'])
def do_post_create():

    data = { 'username' : libapi.authenticate(request) }

    if not data['username']:
        return jsonify({'error': 'invalid authentication'}), 401
