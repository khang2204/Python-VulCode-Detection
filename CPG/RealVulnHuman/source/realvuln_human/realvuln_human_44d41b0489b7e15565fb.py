db.session.commit()

    return jsonify({
        'message': 'Transfer successful',
        'transaction': transaction.to_dict()
    })

@transaction_bp.route('/api/transactions', methods=['GET'])
@token_required
def get_transactions(current_user):
    user_id = request.args.get('user_id', current_user.id)

    query = f'SELECT * FROM "Transaction" WHERE sender_id = {user_id} OR receiver_id = {user_id} ORDER BY created_at DESC'
    result = db.session.execute(query)
    transactions = result.fetchall()

    return jsonify([{
        'id': t[0],
        'sender_id': t[1],
        'receiver_id': t[2], 
        'amount': float(t[3]),
        'description': t[4],
        'status': t[5],
        'created_at': t[6],
