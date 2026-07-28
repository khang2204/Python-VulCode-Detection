def get_all_books_count():...
"""docstring"""
stmt = """
        select count(*) from books as b
        left outer join collaborations as c on c.book_id=b.id
        left outer join authors as a on a.id=c.author_id
        left join series as s on s.id=b.series_id
        """
csr = get_cursor()
count = csr.execute(stmt).fetchone()[0]
return count
