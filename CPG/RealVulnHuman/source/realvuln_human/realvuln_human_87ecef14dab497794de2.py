'amount': float(t[3]),
        'description': t[4],
        'status': t[5],
        'created_at': t[6],
        'completed_at': t[7]
    } for t in transactions])

@transaction_bp.route('/api/transactions/<int:transaction_id>', methods=['GET'])
@token_required
def get_transaction(current_user, transaction_id):
    transaction = Transaction.query.get(transaction_id)

    if not transaction:
        return jsonify({'error': 'Transaction not found'}), 404

    if transaction.sender_id != current_user.id and transaction.receiver_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    return jsonify({
        'id': transaction.id,
        'sender_id': transaction.sender_id,
