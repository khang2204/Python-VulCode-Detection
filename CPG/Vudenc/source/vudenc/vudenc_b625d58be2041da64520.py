def atfu(urls):...
for user, domain, id1, id2 in r_di.findall(urls):
id_ = id1 + id2
add_target(domain, id_, user)
