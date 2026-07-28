def rffu(urls):...
for user, domain, forum in r_udf.findall(urls):
if len(forum) > 0:
get_forum_id(forum)
logger.info('Removing %s:%s from forums[%s]', user, forum, domain)
forums[domain].remove((user, forum))
