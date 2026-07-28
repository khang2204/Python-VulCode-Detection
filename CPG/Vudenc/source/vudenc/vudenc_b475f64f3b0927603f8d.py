def get_list_context(context=None):...
list_context = frappe._dict(template='templates/includes/blog/blog.html',
    get_list=get_blog_list, hide_filters=True, children=get_children(),
    title=_('Blog'))
category = (frappe.local.form_dict.blog_category or frappe.local.form_dict.
    category)
if category:
category_title = get_blog_category(category)
if frappe.local.form_dict.blogger:
list_context.sub_title = _('Posts filed under {0}').format(category_title)
blogger = frappe.db.get_value('Blogger', {'name': frappe.local.form_dict.
    blogger}, 'full_name')
if frappe.local.form_dict.txt:
list_context.title = category_title
list_context.sub_title = _('Posts by {0}').format(blogger)
list_context.sub_title = _('Filtered by "{0}"').format(frappe.local.
    form_dict.txt)
if list_context.sub_title:
list_context.title = blogger
list_context.parents = [{'name': _('Home'), 'route': '/'}, {'name': 'Blog',
    'route': '/blog'}]
list_context.parents = [{'name': _('Home'), 'route': '/'}]
list_context.update(frappe.get_doc('Blog Settings', 'Blog Settings').
    as_dict(no_default_fields=True))
return list_context
