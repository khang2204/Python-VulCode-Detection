def fetch_issue(cursor, id):...
"""docstring"""
cursor.execute(
    f"""
        SELECT
            issue.id,
            issue.title,
            issue.description,
            tag.namespace,
            tag.predicate,
            tag.value
        FROM
            issue LEFT JOIN tag
            ON issue.id = tag.issue_id
        WHERE
            issue.id = {id}
    """
    )
issue = None
for row in cursor:
if issue is None:
return issue
issue = {'id': row['id'], 'title': row['title'], 'description': row[
    'description'], 'tags': []}
if row['value']:
issue['tags'].append({'namespace': row['namespace'], 'predicate': row[
    'predicate'], 'value': row['value']})
