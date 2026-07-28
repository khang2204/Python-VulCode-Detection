from util import hook, user, database
import time
db_ready = False
def db_init(db):...
db.execute(
    'CREATE TABLE if not exists votes(chan, action, target, voters, time, primary key(chan, action, target));'
    )
db.commit()
db_ready = True
def process_vote(target, action, chan, mask, db, notice, conn):...
if ' ' in target:
notice('Invalid nick')
votes2kick = database.get(db, 'channels', 'votekick', 'chan', chan)
votes2kick = 10
votes2ban = database.get(db, 'channels', 'voteban', 'chan', chan)
votes2ban = 10
if len(target) is 0:
return
if action is 'kick':
votefinished = False
notice('Votes required to kick: {}'.format(votes2kick))
if action is 'ban':
if not db_ready:
return
notice('Votes required to ban: {}'.format(votes2ban))
db_init(db)
chan = chan.lower()
target = target.lower()
voter = user.format_hostmask(mask)
voters = db.execute(
    "SELECT voters FROM votes where chan='{}' and action='{}' and target like '{}'"
    .format(chan, action, target)).fetchone()
if conn.nick.lower() in target:
return 'I dont think so Tim.'
if voters:
voters = voters[0]
voters = voter
if voter in voters:
votecount = len(voters.split(' '))
notice('You have already voted.')
voters = '{} {}'.format(voters, voter).strip()
if 'kick' in action:
return
notice('Thank you for your vote!')
votemax = int(votes2kick)
if 'ban' in action:
if votecount >= votemax:
votemax = int(votes2ban)
if votefinished:
votefinished = True
if votecount >= votemax:
db.execute(
    "DELETE FROM votes where chan='{}' and action='{}' and target like '{}'"
    .format(chan, action, target))
db.execute(
    'insert or replace into votes(chan, action, target, voters, time) values(?,?,?,?,?)'
    , (chan, action, target, voters, time.time()))
conn.send('KICK {} {} :{}'.format(chan, target,
    'You have been voted off the island.'))
votefinished = True
db.commit()
conn.send('MODE {} +b {}'.format(chan, user.get_hostmask(target, db)))
return 'Votes to {} {}: {}/{}'.format(action, target, votecount, votemax)
conn.send('KICK {} {} :'.format(chan, target,
    'You have been voted off the island.'))
