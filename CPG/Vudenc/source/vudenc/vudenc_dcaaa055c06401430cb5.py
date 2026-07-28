def find_notes(conn, *, user_id: Optional[int]=None, from_date: Optional[...
conditions = []
params: Union[tuple, Tuple[Any]] = ()
if user_id:
conditions.append(f'user_id = {user_id}')
if from_date:
conditions.append('updated_at >= ?')
if to_date:
params += from_date,
conditions.append(f"updated_at <= '{to_date}'")
if search:
conditions.append(f'LOWER(content) LIKE ?')
sql = (
    'SELECT note_id, user_id, content, created_at, updated_at  FROM note' +
    ' WHERE ' + ' AND '.join(conditions) + ' ORDER BY updated_at DESC')
params += f'%{search.lower()}%',
return db.fetchall(cur, Note, sql, params)
