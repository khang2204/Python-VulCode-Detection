def get_context(self, context):...
if not cint(self.published):
context.full_name = get_fullname(self.owner)
context.updated = global_date_format(self.published_on)
if self.blogger:
context.blogger_info = frappe.get_doc('Blogger', self.blogger).as_dict()
context.description = self.blog_intro or self.content[:140]
context.metatags = {'name': self.title, 'description': context.description}
if '<!-- markdown -->' in context.content:
context.content = markdown(context.content)
image = find_first_image(self.content)
if image:
context.metatags['image'] = image
context.comment_list = get_comment_list(self.doctype, self.name)
if not context.comment_list:
context.comment_text = _('No comments yet')
if len(context.comment_list) == 1:
context.category = frappe.db.get_value('Blog Category', context.doc.
    blog_category, ['title', 'route'], as_dict=1)
context.comment_text = _('1 comment')
context.comment_text = _('{0} comments').format(len(context.comment_list))
context.parents = [{'name': _('Home'), 'route': '/'}, {'name': 'Blog',
    'route': '/blog'}, {'label': context.category.title, 'route': context.
    category.route}]
