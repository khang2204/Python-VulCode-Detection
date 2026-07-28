else:
    if not verify_jwt(token):
        return jsonify({'Error': 'Invalid Token'}),403
    else:
        content = request.json
        results = []
        if content:
            try:
                search_term = content['search']
                print(search_term)
                str_query = "SELECT first_name, last_name, username FROM customer WHERE username = '%s';" % search_term
                # mycust = Customer.query.filter_by(username = search_term).first()
                # return jsonify({'Customer': mycust.username, 'First Name': mycust.first_name}),200

                search_query = db.engine.execute(str_query)
                for result in search_query:
                    results.append(list(result))
                print(results)
                return jsonify(results),200
            except Exception as e:
                template = '''<html>
                    <head>
                    <title>Error</title>
                    </head>
                    <body>
