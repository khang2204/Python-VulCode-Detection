def render_link(self):...
if not hasattr(self.object, 'get_absolute_url'):
return format_html('<td><a href="{}">{}</a></td>', self.object.
    get_absolute_url(), self.format(self.get_value()))
