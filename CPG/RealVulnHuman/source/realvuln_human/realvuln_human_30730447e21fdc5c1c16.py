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

@auth_bp.route('/api/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    profile_data = current_user.get_profile()
    return jsonify({
        'fullName': profile_data.get('fullName', current_user.username),
        'email': current_user.email,
        'phone': profile_data.get('phone', ''),
        'address': profile_data.get('address', '')
