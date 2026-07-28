if user and User.query.get(user[0]).check_password(password):
    user_obj = User.query.get(user[0])

    token = jwt.encode(
        {
            'user_id': user[0],
            'username': username,
            'exp': datetime.utcnow() + timedelta(days=1)
        },
        'secret',
        algorithm='HS256'
    )

    login_attempt = LoginAttempt(
        username=username,
        ip_address=request.remote_addr,
        created_at=datetime.utcnow(),
        success=True
    )
    db.session.add(login_attempt)
