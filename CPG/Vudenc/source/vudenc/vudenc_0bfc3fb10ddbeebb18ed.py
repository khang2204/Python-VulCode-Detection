def make_route(self):...
if not self.route:
return frappe.db.get_value('Blog Category', self.blog_category, 'route'
    ) + '/' + self.scrub(self.title)
