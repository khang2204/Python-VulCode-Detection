from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.render import clear_cache
from frappe.utils import today, cint, global_date_format, get_fullname, strip_html_tags, markdown
from frappe.website.utils import find_first_image, get_comment_list
website = frappe._dict(order_by='published_on desc')
def make_route(self):...
if not self.route:
return frappe.db.get_value('Blog Category', self.blog_category, 'route'
    ) + '/' + self.scrub(self.title)
def get_feed(self):...
return self.title
