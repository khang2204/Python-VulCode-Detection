def unlock_achievement(achievement_id, player_id):...
"""docstring"""
newly_unlocked = False
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute('SELECT type FROM achievement_definitions WHERE id = %s',
    achievement_id)
achievement = cursor.fetchone()
if achievement['type'] != 'STANDARD':
cursor.execute(
    """SELECT
                            state
                        FROM player_achievements
                        WHERE achievement_id = %s AND player_id = %s"""
    , (achievement_id, player_id))
player_achievement = cursor.fetchone()
new_state = 'UNLOCKED'
newly_unlocked = not player_achievement or player_achievement['state'
    ] != 'UNLOCKED'
cursor.execute(
    """INSERT INTO player_achievements (player_id, achievement_id, state)
                        VALUES
                            (%(player_id)s, %(achievement_id)s, %(state)s)
                        ON DUPLICATE KEY UPDATE
                            state = VALUES(state)"""
    , {'player_id': player_id, 'achievement_id': achievement_id, 'state':
    new_state})
return dict(newly_unlocked=newly_unlocked)
