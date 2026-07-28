return jsonify({'error': 'Receiver not found'}), 404

    transaction = Transaction(
        sender_id=current_user.id,
        receiver_id=receiver.id,
        amount=amount,
        description=description,
        status='completed',
        completed_at=datetime.utcnow()
    )
    if current_user.balance < amount:
        return jsonify({'error': 'Insufficient balance'}), 400  

    current_user.balance -= amount
    receiver.balance += amount

    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        'message': 'Transfer successful',
        'transaction': transaction.to_dict()
    })

@transaction_bp.route('/api/transactions', methods=['GET'])
@token_required
def get_transactions(current_user):
    user_id = request.args.get('user_id', current_user.id)
