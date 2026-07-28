def run(self, iden, solution):...
if not c.user_is_loggedin or c.user.needs_captcha():
if not captcha.valid_solution(iden, solution):
c.errors.add(errors.BAD_CAPTCHA)
