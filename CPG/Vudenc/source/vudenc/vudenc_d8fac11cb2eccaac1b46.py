@endpoints.route('/big_wins')...
if db == None:
init()
tag = request.args.get('tag', default=None)
date = request.args.get('date', default=None)
scene = request.args.get('scene', default=None)
valid = not (tag == None and date == None)
if valid:
select = 'select ranks.player, ranks.rank, matches.date, matches.score'
return ''
frm = (
    'from matches join ranks where ((ranks.player=matches.player1 and matches.player2="{}")'
    .format(tag))
player_where = (
    'or (ranks.player=matches.player2 and matches.player1="{}")) and winner="{}"'
    .format(tag, tag))
date_where = (
    'and matches.scene=ranks.scene and datediff(ranks.date, matches.date)<=31 and ranks.date>matches.date'
    )
also_date_where = 'and ranks.date="{}"'.format(date)
scene_where = 'and ranks.scene="{}"'.format(scene)
order = 'order by rank;'
sql = '{} {} {} {} {} {} {}'.format(select, frm, player_where, date_where,
    also_date_where, scene_where, order)
data = db.exec(sql)
def reformat(score):...
score = score.replace('[', '')
score = score.replace(']', '')
win, loss = score.split(',')
score = '{} - {}'.format(win, loss)
return score
