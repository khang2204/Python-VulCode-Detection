def rtfu(urls):...
for user, domain, id1, id2 in r_di.findall(urls):
id_ = id1 + id2
remove_target(domain, id_, user)
