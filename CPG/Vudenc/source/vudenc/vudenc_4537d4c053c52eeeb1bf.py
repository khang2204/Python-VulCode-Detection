def add_limit(self):...
if self.limit_page_length:
return 'limit %s, %s' % (self.limit_start, self.limit_page_length)
return ''
