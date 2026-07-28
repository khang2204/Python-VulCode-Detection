return render_template('index.html', urls = links)


@app.route('/register/user', methods = ['POST'])
def reg_customer():
    try:
        content = request.json
        if content:
            username = content['username']
            password = content['password']
            hash_pass = hashlib.md5(password).hexdigest()
            new_user = User(username, hash_pass)
            db.session.add(new_user)
            db.session.commit()
            user_created = 'User: {0} has been created'.format(username)
            return jsonify({'Created': user_created}),200
    except Exception as e:
        return jsonify({'Error': str(e.message)}),404

@app.route('/register/customer', methods = ['POST'])
def reg_user():
