comment = params.get('comment', '')[0]
    cursor.execute('INSERT INTO comments VALUES(NULL, ?, ?)', [comment, time.ctime()])
    connection.commit()
    content = 'Thank you for leaving the comment. Please click <a href=/guestbook?comment=>here</a> to see all comments...'
else:
    cursor.execute("SELECT id, comment, time FROM comments")
    rows = ""
    for row in cursor.fetchall():
        columns = ""
        for column in row:
            columns += "".join("<td>{}</td>".format("-" if column is None else column))
        rows += "".join("<tr>{}</tr>".format(columns))

    content = '''
        <div><span>Comment(s):</span></div>
        <table>
            <thead>
                <th>id</th>
                <th>comment</th>
                <th>time</th>
            </thead>
