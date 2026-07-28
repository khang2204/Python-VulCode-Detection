def check_password_conformity(pw1: str, pw2: str):...
if not pw1 == pw2:
return False
if len(pw1) < 6:
return False
if pw1.isupper():
return False
if pw1.islower():
return False
return True
