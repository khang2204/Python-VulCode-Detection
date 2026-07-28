q += ' OFFSET + %(offset)s '
        params['offset'] = offset
    async with conn.cursor() as cur:
        await cur.execute(q, **params)
        result = await cur.fetchall()
        return [Course.from_raw(r) for r in result]

@staticmethod
async def create(conn: Connection, title: str,
                 description: Optional[str] = None):
    q = ('INSERT INTO courses (title, description) '
         'VALUES (%(title)s, %(description)s)')
    async with conn.cursor() as cur:
        await cur.execute(q, {'title': title,
                              'description': description})
