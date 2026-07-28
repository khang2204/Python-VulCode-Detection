def db_init(db):...
db.execute(
    'CREATE TABLE if not exists votes(chan, action, target, voters, time, primary key(chan, action, target));'
    )
db.commit()
db_ready = True
