def get_sort_clause(sort_col, sort_dir):...
column_sort_list = {'Title': 'lower(b.Title) {0}', 'ISBN': 'b.ISBN {0}',
    'Volume': 'b.Volume {0}', 'Series': 'lower(s.name) {0}', 'Published':
    'b.Published {0}', 'Category': 'lower(b.Category) {0}', 'Status':
    'lower(b.Status) {0}', 'CoverType': 'lower(b.CoverType) {0}', 'Notes':
    'lower(b.Notes) {0}', 'id': 'b.id {0}', 'Author':
    'lower(a.LastName) {0}, lower(a.FirstName) {0}'}
sd = 'asc'
if sort_dir.lower() == 'desc':
sd = 'desc'
return column_sort_list[sort_col].format(sd)
