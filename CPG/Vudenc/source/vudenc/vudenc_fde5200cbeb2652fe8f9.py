def run(self, emails0):...
emails = set(self.separator.findall(emails0) if emails0 else [])
failures = set(e for e in emails if not self.email_re.match(e))
emails = emails - failures
if self.num > 0 and len(emails) + len(failures) > self.num:
if self.num == 1:
if failures:
c.errors.add(errors.BAD_EMAILS, {'emails': '"%s"' % emails0})
c.errors.add(errors.TOO_MANY_EMAILS, {'num': self.num})
c.errors.add(errors.BAD_EMAILS, {'emails': ', '.join(failures)})
if not emails:
c.errors.add(errors.NO_EMAILS)
return list(emails)[0] if self.num == 1 else emails
