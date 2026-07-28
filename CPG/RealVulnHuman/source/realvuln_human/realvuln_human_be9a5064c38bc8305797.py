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
            current_user.set_profile(profile_data)
            db.session.commit()
            return jsonify({'message': 'Profile imported successfully'})
        return jsonify({'error': 'Invalid profile format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
