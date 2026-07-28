'ORDER BY date')
    params = (course_id,)
    async with conn.cursor() as cur:
        await cur.execute(q, params)
        result = await cur.fetchall()
        return [Review.from_raw(r) for r in result]

@staticmethod
async def create(conn: Connection, course_id: int,
                 review_text: str):
    q = ('INSERT INTO course_reviews (course_id, review_text) '
         'VALUES (%(course_id)s, %(review_text)s)')
    params = {'course_id': course_id,
              'review_text': review_text}
    async with conn.cursor() as cur:
        await cur.execute(q, params)
