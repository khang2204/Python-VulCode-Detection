def search_for_books_by_page(page, pagesize, author_id, series_id,...
inputs = {'limit': pagesize, 'offset': int(page * pagesize)}
wh = ''
if author_id:
wh = 'where c.author_id=' + str(author_id)
if series_id:
if search_arg:
wh = 'where b.series_id=' + str(series_id)
s = '%' + search_arg + '%'
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
        {1}
        order by {0}
        limit :limit offset :offset
        """
    .format(get_sort_clause(sort_col, sort_dir), wh))
inputs['like'] = s
csr = get_cursor()
wh = 'where b.Title like :like'
rst = csr.execute(stmt, inputs)
rows = rows2list(rst)
return {'rows': rows, 'count': get_filtered_books_count(author_id,
    series_id, search_arg)}
