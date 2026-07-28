def validate(self):...
super(BlogPost, self).validate()
if not self.blog_intro:
self.blog_intro = self.content[:140]
if self.blog_intro:
self.blog_intro = strip_html_tags(self.blog_intro)
self.blog_intro = self.blog_intro[:140]
if self.published and not self.published_on:
self.published_on = today()
frappe.db.sql(
    """update tabBlogger set posts=(select count(*) from `tabBlog Post`
			where ifnull(blogger,'')=tabBlogger.name)
			where name=%s"""
    , (self.blogger,))
