def get_books_by_page(page, pagesize, sort_col, sort_dir):...
stmt = (
    """
        select b.*,
        case when length(a.FirstName) > 0
            then (a.LastName || ", " || a.FirstName)
            else a.LastName
            end as Author,
        s.name as Series from books as b
        left outer join collaborations as c on c.book_id=b.id
        left outer join authors as a on a.id=c.author_id
        left join series as s on s.id=b.series_id
        order by {0}
        limit :limit offset :offset
        """
    .format(get_sort_clause(sort_col, sort_dir)))
inputs = {'limit': pagesize, 'offset': int(page * pagesize)}
csr = get_cursor()
rst = csr.execute(stmt, inputs)
rows = rows2list(rst)
return {'rows': rows, 'count': get_all_books_count()}
