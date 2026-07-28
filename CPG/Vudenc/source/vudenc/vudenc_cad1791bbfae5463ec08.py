def findNPC(race, classe, sex, level):...
c, conn = getConnection()
date = now()
c.execute("select image, avg(legit) as l FROM npc WHERE race='" + race +
    "' AND class='" + classe + "' AND sex='" + sex +
    "' GROUP BY image HAVING l > 5 ORDER BY SUM(legit) DESC;")
conn.commit()
out = c.fetchmany(5)
conn.close()
return out
