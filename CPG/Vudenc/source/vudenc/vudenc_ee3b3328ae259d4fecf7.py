def reformat(score):...
score = score.replace('[', '')
score = score.replace(']', '')
win, loss = score.split(',')
score = '{} - {}'.format(loss, win)
return score
