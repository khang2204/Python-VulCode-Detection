def update_issue(cursor, id, fields):...
"""docstring"""
updated_fields = {}
if 'title' in fields:
updated_fields['title'] = fields['title']
if 'description' in fields:
updated_fields['description'] = fields['description']
set_clause_args = ', '.join(map(lambda kv: f'{kv[0]} = "{kv[1]}"',
    updated_fields.items()))
if len(updated_fields) != 0:
cursor.execute(
    f"""
            UPDATE issue
            SET {set_clause_args}
            WHERE id = {id}
        """
    )
cursor.execute(
    f"""
        DELETE FROM tag
        WHERE issue_id = {id}
    """)
for tag in fields.get('tags', []):
cursor.execute(
    f"""
            INSERT INTO tag (
                namespace,
                predicate,
                value,
                issue_id
            )
            VALUES (
                "{tag['namespace']}",
                "{tag['predicate']}",
                "{tag['value']}",
                "{id}"
            )
        """
    )
