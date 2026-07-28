def whitelist_check(ctx):...
for x in role_whitelist:
if x in [y.id for y in ctx.message.author.roles]:
return True
return False
