username=username,
        ip_address=request.remote_addr,
        created_at=datetime.utcnow(),
        success=False
    )
    db.session.add(login_attempt)
    db.session.commit()

    return jsonify({'error': 'Invalid username or password'}), 401

@auth_bp.route('/api/logout', methods=['POST'])
@token_required
def logout(current_user):
    # JWT tokens can't be invalidated server-side
    # Client should remove the token
    return jsonify({'message': 'Logged out successfully'})

@auth_bp.route('/api/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'balance': float(current_user.balance),
        'profile': current_user.get_profile()
    })
