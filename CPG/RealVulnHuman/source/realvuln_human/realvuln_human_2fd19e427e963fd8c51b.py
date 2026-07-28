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
                        <h1>Oops Error Occurred</h1>
                        <h3>%s</h3>
                        </body>
                        </html>
                        ''' % str(e)
                    return render_template_string(template, dir=dir, help=help, locals=locals), 404


@app.route("/xxe")
def index():
    return render_template(
        'test.html')


@app.route("/xxe_uploader", methods=['GET', 'POST'])  # /<string:name>/")
def hello():
