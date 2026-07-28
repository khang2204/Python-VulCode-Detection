def clear_blog_cache():...
for blog in frappe.db.sql_list(
clear_cache(blog)
clear_cache('writers')
