if offset is not None:
        q += ' OFFSET + %(offset)s '
        params['offset'] = offset
    async with conn.cursor() as cur:
        await cur.execute(q, params)
        results = await cur.fetchall()
        return [Student.from_raw(r) for r in results]

@staticmethod
async def create(conn: Connection, name: str):
    q = ("INSERT INTO students (name) "
         "VALUES ('%(name)s')" % {'name': name})
    async with conn.cursor() as cur:
        await cur.execute(q)
