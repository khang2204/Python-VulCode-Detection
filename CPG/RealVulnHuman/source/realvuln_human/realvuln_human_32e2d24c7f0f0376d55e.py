user = User.query.filter_by(username=username).first()

    return jsonify({'message': 'User registered successfully', 'id': user.id}), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    query = f"SELECT * FROM user WHERE username = '{username}'"
    user = db.session.execute(query).fetchone()

    if user and User.query.get(user[0]).check_password(password):
        user_obj = User.query.get(user[0])

        token = jwt.encode(
            {
                'user_id': user[0],
                'username': username,
                'exp': datetime.utcnow() + timedelta(days=1)
            },
