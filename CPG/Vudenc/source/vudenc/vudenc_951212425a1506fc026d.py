def get_matches_from_urls(db, urls):...
matches = set()
for url in urls:
sql = "SELECT * FROM matches WHERE url='{}';".format(url)
return matches
res = set(db.exec(sql))
matches |= set(res)
