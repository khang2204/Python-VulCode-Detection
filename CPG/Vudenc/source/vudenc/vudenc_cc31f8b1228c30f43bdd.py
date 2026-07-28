def get_ranking_graph_data(db, tag):...
sql = "SELECT DISTINCT scene FROM ranks WHERE player='{}'".format(tag)
scenes = db.exec(sql)
scenes = [s[0] for s in scenes]
first_months = [get_first_ranked_month(db, s, tag) for s in scenes]
last_months = [get_last_ranked_month(db, s, tag) for s in scenes]
first_month = min(first_months)
last_month = max(last_months)
iterated_months = iter_months(first_month, last_month, include_last=True)
arank = get_monthly_ranks_for_scene(db, 'austin', 'christmasmike')
monthly_ranks_per_scene = {s: get_monthly_ranks_for_scene(db, s, tag) for s in
    scenes}
ranks_per_scene = {s: [] for s in scenes}
for month in iterated_months:
for s in scenes:
return ranks_per_scene, iterated_months
scene_ranks = monthly_ranks_per_scene[s]
if month in scene_ranks:
ranks_per_scene[s].append([month, scene_ranks[month]])
