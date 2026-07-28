'completed_at': transaction.completed_at.isoformat() if transaction.completed_at else None
    })

@transaction_bp.route('/api/transactions/search', methods=['GET'])
@token_required
def search_transactions(current_user):
    search_term = request.args.get('description', '')

    # VULNERABLE CODE: Direct string concatenation in SQL query
    # This is deliberately vulnerable to SQL injection for educational purposes
    query = f"SELECT * FROM \"transaction\" WHERE (sender_id = {current_user.id} OR receiver_id = {current_user.id}) AND description LIKE '%{search_term}%'"

    result = db.session.execute(query)
    transactions = result.fetchall()

    transaction_list = []
    for t in transactions:
        transaction_list.append({
            'id': t[0],
            'sender_id': t[1],
            'receiver_id': t[2], 
            'amount': float(t[3]),
            'description': t[4],
