def karma_rank(name):...
db = db_connect()
cursor = db.cursor()
cursor.execute(
    """
            SELECT (SELECT COUNT(*) FROM people AS t2 WHERE t2.karma > t1.karma)
            AS row_Num FROM people AS t1 WHERE name='{}'
        """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
rank = cursor.fetchone()[0] + 1
logger.debug('Rank of {} found for name {}'.format(rank, name))
db.close()
return rank
