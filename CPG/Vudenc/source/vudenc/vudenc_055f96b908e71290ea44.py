def get_children():...
return frappe.db.sql(
    """select route as name,
		title from `tabBlog Category`
		where published = 1
		and exists (select name from `tabBlog Post`
			where `tabBlog Post`.blog_category=`tabBlog Category`.name and published=1)
		order by title asc"""
    , as_dict=1)
