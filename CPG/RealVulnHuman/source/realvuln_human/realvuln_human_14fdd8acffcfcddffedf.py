def get_all_users():
    return [User.json(user) for user in User.query.all()]

@staticmethod
def get_all_users_debug():
    return [User.json_debug(user) for user in User.query.all()]

@staticmethod
def get_user(username):
    if vuln:  # SQLi Injection
        user_query = f"SELECT * FROM users WHERE username = '{username}'"
        query = db.session.execute(text(user_query))
        ret = query.fetchone()
        if ret:
            fin_query = '{"username": "%s", "email": "%s"}' % (ret[1], ret[3])
        else:
            fin_query = None
    else:
        fin_query = User.query.filter_by(username=username).first()
    return fin_query

@staticmethod
