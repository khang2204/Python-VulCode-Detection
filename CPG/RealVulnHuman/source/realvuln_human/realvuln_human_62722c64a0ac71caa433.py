return {'resp': 'done'}
    elif user:
        db_client.vfapi.users.delete_one({'address': user.address})
        await run_sql_query(f'DELETE FROM users WHERE address = {user.address};', commit=True)
    return {'resp': '!done'}

@app.get('/reset')
def reset_page():
    return {'resp': 'Please issue a POST request to the same endpoint in order to actually reset the database.'}

@app.post('/reset')
async def reset_database():
    remove(f'{DB_FILENAME}.sql.db')
    rmtree(f'{DB_FILENAME}.nosql.db')
    await init_db()
    return {'resp': 'done'}

@app.get('/favicon.ico')
def return_favicon():
    return FileResponse('./static/img/favicon.ico')

@app.get('/robots.txt')
def return_robots_txt():
    return FileResponse('./static/robots.txt')

@app.get('/.well-known/security.txt')
