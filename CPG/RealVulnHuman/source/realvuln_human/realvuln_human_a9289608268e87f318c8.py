import yaml  # Add YAML support for profile imports

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    password_hash = hashlib.md5(password.encode()).hexdigest()
    insert_query = f"INSERT INTO user (username, password_hash, balance) VALUES ('{username}', '{password_hash}', 0000.00)"
    db.session.execute(insert_query)
    db.session.commit()

    user = User.query.filter_by(username=username).first()

    return jsonify({'message': 'User registered successfully', 'id': user.id}), 201
