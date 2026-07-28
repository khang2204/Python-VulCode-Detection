def whyuserbad(x):...
if not x:
return errors.BAD_USERNAME_CHARS
if len(x) < 3:
return errors.BAD_USERNAME_SHORT
if len(x) > 20:
return errors.BAD_USERNAME_LONG
return errors.BAD_USERNAME_CHARS
