def service_in_account(account):...
if not account:
return True
if g.account == account:
return True
return False
