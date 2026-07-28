return jsonify({
        'message': 'Profile updated successfully',
        'profile': {
            'fullName': profile_data['fullName'],
            'email': current_user.email,
            'phone': profile_data['phone'],
            'address': profile_data['address']
        }
    })

@auth_bp.route('/api/update-password', methods=['POST'])
@token_required
def update_password(current_user):
    data = request.get_json()
    user_id = data.get('user_id')
    new_password = data.get('new_password')

    user = User.query.get(user_id)
    if user:
        user.set_password(new_password)
        db.session.commit()
        return jsonify({'message': 'Password updated'})
    return jsonify({'error': 'User not found'}), 404 

@auth_bp.route('/api/profile/import', methods=['POST'])
@token_required
def import_profile(current_user):
    try:
        profile_yaml = request.get_json().get('profile_yaml', '')
        # Vulnerable: directly loads YAML that could contain malicious code
        profile_data = yaml.load(profile_yaml, Loader=yaml.Loader)

        if isinstance(profile_data, dict):
