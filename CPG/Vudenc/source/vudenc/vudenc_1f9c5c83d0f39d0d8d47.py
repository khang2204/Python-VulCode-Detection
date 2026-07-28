def update_video_position(id, position, next_position, db):...
db.execute(
    'UPDATE video SET position = Case position When {position} Then {next_position} Else position + 1 End WHERE position BETWEEN {next_position} AND {position};'
    .format(position=position, next_position=next_position))
