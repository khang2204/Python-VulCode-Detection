from decimal import Decimal
from auth import token_required

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/api/transfer', methods=['POST'])
@token_required
def transfer(current_user):
    data = request.get_json()
    to_user_id = data.get('to_user_id')
    amount = Decimal(str(data.get('amount', 0)))
    description = data.get('description', '')

    receiver = User.query.get(to_user_id)

    if not receiver:
        return jsonify({'error': 'Receiver not found'}), 404

    transaction = Transaction(
        sender_id=current_user.id,
        receiver_id=receiver.id,
