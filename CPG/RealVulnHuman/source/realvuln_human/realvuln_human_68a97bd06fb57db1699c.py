async def index(request: Request):
    app: Application = request.app
    auth_user = await get_auth_user(request)

    session = await get_session(request)
    last_visited = session.get('last_visited', 'never')
    session['last_visited'] = datetime.now().isoformat()

    errors = []

    if request.method == 'POST':
        if auth_user:
            raise HTTPForbidden()
        data = await request.post()
        username = data['username']
        password = data['password']
        async with app['db'].acquire() as conn:
            user = await User.get_by_username(conn, username)
        if user and user.check_password(password):
            session['user_id'] = user.id
            auth_user = user
        else:
            errors.append('Invalid username or password')
    return {'last_visited': last_visited,
            'errors': errors,
            'auth_user': auth_user}


@template('students.jinja2')
async def students(request: Request):
    app: Application = request.app
    if request.method == 'POST':
        data = await request.post()
