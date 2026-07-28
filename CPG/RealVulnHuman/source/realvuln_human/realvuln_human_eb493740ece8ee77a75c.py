for data in user_data: data.pop('_id'); data.pop('password')
    if len(user_data) == 1: return user_data[0]
    return tuple(user_data)

@app.get('/')
def root():
    return {'goto': '/docs'}

@app.get('/select')
async def sql_return_users_from_username(username: str):
    resp = await run_sql_query(f'SELECT * FROM users WHERE username = "{username}";')
    return resp

@app.put('/user')
async def put_user(user: User):
    user.password = md5(user.password.encode()).hexdigest()
    query = f'''
INSERT INTO users (
                    name,
                    username,
                    password,
