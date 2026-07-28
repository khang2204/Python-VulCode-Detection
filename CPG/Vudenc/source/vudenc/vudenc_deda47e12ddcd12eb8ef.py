@FirstZeros.route('/')...
start = request.args.get('start', None, float)
end = request.args.get('end', None, float)
limit = request.args.get('limit', 100, int)
degree = request.args.get('degree', None, int)
if limit > 1000:
limit = 1000
if limit < 0:
limit = 100
title = 'Search for First Zeros of L-functions'
bread = [('L-functions', url_for('l_functions.l_function_top_page')), (
    'First Zeros Search', ' ')]
return render_template('first_zeros.html', start=start, end=end, limit=
    limit, degree=degree, title=title, bread=bread)
