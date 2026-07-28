@admin_required
def delete(self, id):
    message = Message.query.filter_by(id=id).first()
    if not message:
        return jsonify(API_STATUS_ERROR)
    db.session.delete(message)
    db.session.commit()

    return jsonify(API_STATUS_SUCCESS)

def post(self):
    data = request.get_json()
    if not data:
        return API_STATUS_ERROR
    message = data.get('message', None)
    if not message:
        return API_STATUS_ERROR
    from_user = data.get('from_user', 'Anonymous')

    new_message = Message(message=message, from_user=from_user)
    db.session.add(new_message)
    db.session.commit()

    return jsonify(API_STATUS_SUCCESS)

@route('/acknowledge/<id>', methods=['POST'])
@admin_required
def acknowledge_message(self, id):
    Message.query.filter_by(id=id).update({
        'acknowledged': True
    })
    db.session.commit()

    return jsonify(API_STATUS_SUCCESS)
