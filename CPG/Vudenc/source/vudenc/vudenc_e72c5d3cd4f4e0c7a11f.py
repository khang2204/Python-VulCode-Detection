def run(self, tag_field):...
tags = []
if tag_field:
tags = [x for x in self.comma_sep.split(tag_field) if x == _force_ascii(x)]
return tags
