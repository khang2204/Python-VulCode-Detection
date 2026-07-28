'username': user.username,
        'password': user.password,
        'address': user.address,
        'email': user.email,
        'contact': user.contact
        })
    return {'resp': 'done'}

@app.get('/find')
async def nosql_return_users_from_username(username: str):
    return get_nosql_users({'username': username})

@app.post('/find')
async def nosql_return_users(request: Request):
    query = await request.json()
    return get_nosql_users(query)

@app.delete('/user')
async def delete_user(username: Optional[str] = '', user: Optional[User] = None):
    if username:
        db_client.vfapi.users.delete_one({'username': username})
