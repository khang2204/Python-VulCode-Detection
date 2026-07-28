@app.route('/get/<cust_id>', methods = ['GET'])
def get_customer(cust_id):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'Error': 'Not Authenticated!'}), 403
    else:
        if not insecure_verify(token):
            return jsonify({'Error': 'Invalid Token'}), 403
        else:
            if cust_id:
                customer_record = Customer.query.get(cust_id)
                if customer_record:
                    customer_dict = {'id': customer_record.id, 'firstname': customer_record.first_name,
                                 'lastname': customer_record.last_name, 'email': customer_record.email,
                                 'cc_num': customer_record.ccn, 'username': customer_record.username
                                }
                    return jsonify(customer_dict),200
                else:
                    return jsonify({'Error': 'No Customer Found'}),404
            else:
                return jsonify({'Error': 'Invalid Request'}),400
