def played_during_month(db, scene, tag, date):...
tournaments = get_tournaments_during_month(db, scene, date)
if player_in_url(db, tag, urls=tournaments):
return True
return False
