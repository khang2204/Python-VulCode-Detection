def get_task_uplaod_id(n):...
query = """
    SELECT *
    FROM (
        SELECT row_number() over (ORDER By upload_timestamp DESC) as rownumber, *
        FROM upload_log
    ) as foo
    where rownumber = %(n)s
    """
df = pd.read_sql(query, con=db.engine, params={'n': n})
return df
