@endpoints.route('/tournament_losses')...
if db == None:
init()
tag = request.args.get('tag', default=None)
date = request.args.get('date', default=None)
if tag and date:
sql = (
    "select player1, place, date, score from matches join placings on matches.url=placings.url and matches.player1=placings.player                 where winner!='{}' and player2='{}' and date='{}';"
    .format(tag, tag, date))
return ''
data = db.exec(sql)
sql = (
    "select player2, place, date, score from matches join placings on matches.url=placings.url and matches.player2=placings.player                 where winner!='{}' and player1='{}' and date='{}';"
    .format(tag, tag, date))
data = data + db.exec(sql)
data = [r for r in data]
data.sort(key=lambda x: int(x[1]))
def reformat(score):...
score = score.replace('[', '')
score = score.replace(']', '')
win, loss = score.split(',')
score = '{} - {}'.format(win, loss)
return score
