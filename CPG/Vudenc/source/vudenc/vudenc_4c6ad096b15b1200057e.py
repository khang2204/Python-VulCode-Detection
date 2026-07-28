def get_filtered_books_count(author_id, series_id, search_arg):...
wh = ''
parameters = ()
if author_id:
wh = 'where c.author_id=' + str(int(author_id))
if series_id:
if search_arg:
wh = 'where b.series_id=' + str(int(series_id))
s = '%' + search_arg + '%'
stmt = (
    """
        select count(*) from books as b
        left outer join collaborations as c on c.book_id=b.id
        left outer join authors as a on a.id=c.author_id
        left join series as s on s.id=b.series_id
        {0}
        """
    .format(wh))
parameters += s.encode('utf-8'),
csr = get_cursor()
wh = 'where b.Title like ?'
if len(parameters) > 0:
count = csr.execute(stmt, parameters).fetchone()[0]
count = csr.execute(stmt).fetchone()[0]
return count
