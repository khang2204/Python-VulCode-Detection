def get_blog_list(doctype, txt=None, filters=None, limit_start=0,...
conditions = []
if filters:
if filters.blogger:
if txt:
conditions.append('t1.blogger="%s"' % frappe.db.escape(filters.blogger))
if filters.blog_category:
conditions.append('(t1.content like "%{0}%" or t1.title like "%{0}%")'.
    format(frappe.db.escape(txt)))
if conditions:
conditions.append('t1.blog_category="%s"' % frappe.db.escape(filters.
    blog_category))
frappe.local.no_cache = 1
query = (
    """		select
			t1.title, t1.name, t1.blog_category, t1.route, t1.published_on,
				t1.published_on as creation,
				t1.content as content,
				ifnull(t1.blog_intro, t1.content) as intro,
				t2.full_name, t2.avatar, t1.blogger,
				(select count(name) from `tabCommunication`
					where
						communication_type='Comment'
						and comment_type='Comment'
						and reference_doctype='Blog Post'
						and reference_name=t1.name) as comments
		from `tabBlog Post` t1, `tabBlogger` t2
		where ifnull(t1.published,0)=1
		and t1.blogger = t2.name
		%(condition)s
		order by published_on desc, name asc
		limit %(start)s, %(page_len)s"""
     % {'start': limit_start, 'page_len': limit_page_length, 'condition': 
    ' and ' + ' and '.join(conditions) if conditions else ''})
posts = frappe.db.sql(query, as_dict=1)
for post in posts:
post.cover_image = find_first_image(post.content)
return posts
post.published = global_date_format(post.creation)
post.content = strip_html_tags(post.content[:340])
if not post.comments:
post.comment_text = _('No comments yet')
if post.comments == 1:
post.avatar = post.avatar or ''
post.comment_text = _('1 comment')
post.comment_text = _('{0} comments').format(str(post.comments))
post.category = frappe.db.get_value('Blog Category', post.blog_category, [
    'route', 'title'], as_dict=True)
if post.avatar and (not 'http:' in post.avatar and not 'https:' in post.avatar
post.avatar = '/' + post.avatar
