def affu(urls):...
for user, domain, forum in r_udf.findall(urls):
if domain not in forums:
forums[domain] = set()
if len(forum) > 0:
get_forum_id(forum)
logger.info('Appending %s:%s to forums[%s]', user, forum, domain)
forums[domain].add((user, forum))
