auth_header = request.headers['Authorization']
        try:
            token = auth_header.split(" ")[1]  # Bearer <token>
        except IndexError:
            token = auth_header

    if not token:
        return jsonify({'error': 'Token is missing'}), 401

    try:
        data = jwt.decode(token, 'secret', algorithms=['HS256'])
        current_user = User.query.get(data['user_id'])
        if not current_user:
            return jsonify({'error': 'Invalid token'}), 401
        return f(current_user, *args, **kwargs)
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

return decorated
