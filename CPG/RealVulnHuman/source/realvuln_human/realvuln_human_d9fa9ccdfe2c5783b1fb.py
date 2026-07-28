'id': t[0],
        'sender_id': t[1],
        'receiver_id': t[2], 
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
        'receiver_id': transaction.receiver_id,
        'amount': float(transaction.amount),
        'description': transaction.description,
        'status': transaction.status,
        'created_at': transaction.created_at.isoformat(),
        'completed_at': transaction.completed_at.isoformat() if transaction.completed_at else None
    })

@transaction_bp.route('/api/transactions/search', methods=['GET'])
@token_required
def search_transactions(current_user):
    search_term = request.args.get('description', '')

    # VULNERABLE CODE: Direct string concatenation in SQL query
    # This is deliberately vulnerable to SQL injection for educational purposes
    query = f"SELECT * FROM \"transaction\" WHERE (sender_id = {current_user.id} OR receiver_id = {current_user.id}) AND description LIKE '%{search_term}%'"
