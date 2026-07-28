async def get_by_username(conn: Connection, username: str):
    async with conn.cursor() as cur:
        await cur.execute(
            'SELECT id, first_name, middle_name, last_name, '
            'username, pwd_hash, is_admin FROM users WHERE username = %s',
            (username,),
        )
        return User.from_raw(await cur.fetchone())

def check_password(self, password: str):
    return self.pwd_hash == md5(password.encode('utf-8')).hexdigest()
