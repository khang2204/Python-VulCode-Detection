@bp.route('/user_view')...
db = get_db()
sortBy = sort.split('.')[0]
sortOrder = sort.split('.')[1]
query = (
    'SELECT * FROM user AS u LEFT OUTER JOIN (SELECT uid, count(uid) AS follower FROM follows GROUP BY uid) AS f ON u.id = f.uid ORDER BY ? {}'
    .format(sortOrder))
users = db.execute(query, (sortBy,)).fetchall()
return render_template('admin/userview.html', users=users, sort='{}.{}'.
    format(sortBy, sortOrder))
