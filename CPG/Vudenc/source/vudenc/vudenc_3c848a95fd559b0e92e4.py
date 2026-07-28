def rank_check(id, function):...
query = check(id, 'rank', user_table)
rank = query[0][0]
query2 = fetch("SELECT {} FROM {} WHERE FUNCTION = '{}';".format(rank,
    rank_permit_table, function))
if query2[0][0] == True:
return True
return False
