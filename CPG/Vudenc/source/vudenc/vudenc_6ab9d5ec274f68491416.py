def create_issue(cursor, issue):...
"""docstring"""
cursor.execute(
    f"""
        INSERT INTO issue (
            title,
            description
        )
        VALUES (
            "{issue['title']}",
            "{issue.get('description', '')}"
        )
    """
    )
issue_id = cursor.lastrowid
for tag in issue.get('tags', []):
cursor.execute(
    f"""
            INSERT INTO tag (
                namespace,
                predicate,
                value,
                issue_id
            )
            VALUES (
                "{tag.get('namespace', '')}",
                "{tag.get('predicate', '')}",
                "{tag.get('value', '')}",
                "{issue_id}"
            )
        """
    )
return issue_id
