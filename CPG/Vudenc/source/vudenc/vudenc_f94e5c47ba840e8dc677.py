def run(self, domain):...
if domain and (not self.domain_re.match(domain) or domain.endswith(
c.errors.add(errors.BAD_CNAME)
if domain:
return str(domain).lower()
c.errors.add(errors.BAD_CNAME)
