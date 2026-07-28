def before_request():
    g.session = libsession.load(request)

@app.after_request
def add_csp_headers(response):
    if csp:
        response.headers['Content-Security-Policy'] = csp
    return response


app.run(debug=True, host='127.0.1.1', port=5000, extra_files='csp.txt')
